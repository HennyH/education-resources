'use strict';

const e = React.createElement;
const useState = React.useState;
const useLayoutEffect = React.useLayoutEffect;
const useRef = React.useRef;
const DEFAULT_COLOR = "#ffffff";

const useLocalStorage = (key, fallback) => {
    const [value, setValue] = useState(() => {
        const item = window.localStorage.getItem(key);
        return item === null ? fallback : JSON.parse(item);
    });

    function saveAndSetValue(value) {
        window.localStorage.setItem(key, JSON.stringify(value));
        setValue(value);
    }

    return [value, saveAndSetValue];
}

function ColorPalette({ palette, onPaletteChanged }) {

    const olRef = useRef();
    const [importPaletteBinary, setImportPaletteBinary] = useState('')
   
    useLayoutEffect(() => {
        const inputs = olRef.current.querySelectorAll("input");
        for (const input of inputs) {
            input.addEventListener("change", e => {
                changeColor(parseInt(e.target.getAttribute('data-index')), e.target.value);
            });   
        }
    })

    function changeColor(index, newColor) {
        const nextPalette = [...palette];
        nextPalette[index] = newColor;
        onPaletteChanged(nextPalette);
    }

    function addColor() {
        onPaletteChanged([...palette, DEFAULT_COLOR]);
    }

    function removeColor(index) {
        const nextPalette = [...palette];
        nextPalette.splice(index, 1);
        onPaletteChanged(nextPalette);
    }

    function importPalette() {
        const nextPalette = [];
        for (let i = 0; i < importPaletteBinary.length; i += 24) {
            nextPalette.push(`#${parseInt(importPaletteBinary.substring(i, i + 24), 2).toString(16)}`);
        }
        onPaletteChanged(nextPalette);
        setImportPaletteBinary('');
    }

    const paletteBinary = palette
        .map(c => parseInt(c.substring(1), 16).toString(2).padStart(24, "0"))
        .reduce((acc, s) => `${acc}${s}`, '')

    return e("section", null,
        e("h2", null, "Color Palette"),
        e("p", null, "Each color is represented as a hexcode of the form #rrggbb. Each color uses 24 bits to be represented in binary."),
        e("ol", {ref: olRef}, [
            ...palette.map((c, i) => e("li", {key: `${i}${c}`},
                e("input", {type: "color", defaultValue: c, 'data-index': i}),
                e("button", {onClick: () => removeColor(i)}, "Delete")
            )),
            e("li", {key: "new"},
                e("button", {onClick: addColor}, "Add Color")
            )
        ]),
        e("h3", null, "Export Palette"),
        e("span", {className: "binary"}, paletteBinary),
        e("h3", null, "Import Palette"),
        e("input", {type: "text", pattern: '[01]', value: importPaletteBinary, onChange: e => setImportPaletteBinary(e.target.value)}),
        e("button", {onClick: importPalette, disabled: importPaletteBinary == null || importPaletteBinary == undefined || importPaletteBinary.length == 0}, "Import Palette")
    )
}

function PixelGrid({ dimensions, palette, pixels, onDimensionsChanged, onPixelsChanged }) {
    const [importGridBinary, setImportGridBinary] = useState('')

    const keyForPos = (x, y) => `${x}-${y}`;
    const valueForPos = (x, y) => parseInt(pixels[keyForPos(x, y)]);
    const colorForPos = (x, y) => {
        const val = valueForPos(x, y);
        return val > 0 && val <= palette.length ? palette[val - 1] : DEFAULT_COLOR
    }

    function handleDimensionsChagned(w, h) {
        w = isNaN(w) ? 0 : w;
        h = isNaN(h) ? 0 : h;
        onDimensionsChanged({
            ...dimensions,
            w: w !== null ? w : dimensions.w,
            h: h !== null ? h : dimensions.h
        })
    }

    function handlePixelChanged(i, j, value) {
        onPixelsChanged({
            ...pixels,
            [keyForPos(i, j)]: parseInt(value)
        });
    }

    const pixelValuesBinary = new Array(dimensions.h)
        .fill(null)
        .flatMap((_, j) => new Array(dimensions.w)
            .fill(null)
            .map((_, i) => {
                return (valueForPos(i, j) || 0).toString(2).padStart(8, "0");
            }))
        .reduce((agg, s) => `${agg}${s}`, "");
    const dimensionsBinary =  `${dimensions.w.toString(2).padStart(8, "0")}${dimensions.h.toString(2).padStart(8, "0")}`;
    const gridBinary = `${dimensionsBinary}${pixelValuesBinary}`;

    function importGrid() {
        const w = parseInt(importGridBinary.substring(0, 8), 2);
        const h = parseInt(importGridBinary.substring(8, 16), 2);
        const pixels = {}
        for (let j = 0; j < h; j++) {
            for (let i = 0; i < w; i++) {
                const binStart = 16 + (j * w * 8) + (i * 8);
                pixels[keyForPos(i, j)] = parseInt(importGridBinary.substring(binStart, binStart + 8), 2);
            }
        }
        onDimensionsChanged({ w, h });
        onPixelsChanged(pixels);
    }

    function clearGrid() {
        onPixelsChanged({});
    }

    return e("section", null,
        e("h2", null, "Pixel Grid"),
        e("p", null, "The pixel grid is represented by two 8 bit numbers for the width and height of the grid, followed by an 8 bit number for each cell in left-to-right, top-to-bottom order."),
        e("form", null,
            e("label", null, "Width:", e("input", {type: "number", min: 0, value: dimensions.w === 0 ? "" : dimensions.w, onChange: e => handleDimensionsChagned(parseInt(e.target.value), null) })),
            e("label", null, "Height:", e("input", {type: "number", min: 0, value: dimensions.h === 0 ? "" : dimensions.h, onChange: e => handleDimensionsChagned(null, parseInt(e.target.value)) })),
            e("button", {onClick: clearGrid}, "Clear Grid")
        ),
        e("table", null,
            e("tbody", null, new Array(dimensions.h).fill(null).map((_, j) =>
                e("tr", { key: j }, new Array(dimensions.w).fill(null).map((_, i) =>
                    e("td", {key: i, style: { backgroundColor: colorForPos(i, j) } },
                        e("input", {type: "number", min: 1, max: palette.length, value: valueForPos(i, j) || "", onChange: e => handlePixelChanged(i, j, e.target.value), style: { backgroundColor: colorForPos(i, j) } })
                    )
                ))
            ))
        ),
        e("h3", null, "Export Pixel Grid"),
        e("span", {className: "binary"}, gridBinary),
        e("h3", null, "Import Pixel Grid"),
        e("input", {type: "text", pattern: '[01]', value: importGridBinary, onChange: e => setImportGridBinary(e.target.value)}),
        e("button", {onClick: importGrid, disabled: importGridBinary == null || importGridBinary == undefined || importGridBinary.length == 0}, "Import Grid")
    )
}



function App() {
    const [palette, setPalette] = useLocalStorage("palette", [DEFAULT_COLOR]);
    const [dimensions, setDimensions] = useLocalStorage("dimensions", { w: 5, h: 5 });
    const [pixels, setPixels] = useLocalStorage("pixels", {});

    return e("main", null,
        e(ColorPalette, { palette, onPaletteChanged: setPalette }),
        e(PixelGrid, { dimensions, palette, pixels, onDimensionsChanged: setDimensions, onPixelsChanged: setPixels })
    )
}

ReactDOM.render(e(App), document.querySelector("main"));
