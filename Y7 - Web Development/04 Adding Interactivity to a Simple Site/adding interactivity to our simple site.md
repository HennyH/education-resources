---
title: Introduction to JavaScript
---

# Learning Goals

1. Students can include separate CSS and JS files in a HTML file.
2. Students can use `setInterval` to create visual effects on the page.
3. Students can register an event listener.
4. Students can explain how JS can make sites interactive.
    - (1 - 4) Assessed by completion of tasks in this lesson which will be submitted to connect.
5. Students can identify and write CSS selectors, and style elements using basic properties.
   - Measured by Quizziz quiz on CSS. 
  

# Assessment Plan

1. At various stages walk around the class and see if students are keeping up with the activities.

# Materials and Resources

1. gallery, dice and memory files on the shared drive.

# Teaching Strategies

1. Direct instruction.
2. Competition.
3. Quizzes.
4. Self-guided learning.

# Learning Experience (110min)

## Image Gallery (Pt. 1) (15min)

In this section we'll be creating a simple image gallery whose picture changes every _x_ milliseconds, by completing the following steps:

1. Create three files: `gallery.html`, `gallery.js`, `gallery.css` (students copy from shared drive).
2. Use the `html:5` shortcut to fill in the HTML5 boilerplate. Then add a `link:css` to the head, and a `script:src` to the bottom of the body to include our other files.
3. Add a `h1` header of "Flower Gallery", and create an `<img>` with an `id` of `flower-gallery`.
4. Write the JS code to change the image on a given interval, mentioning the following elements:
    - _functions_: a named grouped set of instructions, like a recipe.
    - _urls_: A link to a resource.
    - _parameters_: values which change the operation/result of a function, like spiciness.
    - _modulo_: draw a clock-face and explain `currentPhoto++ % imgUrls.length`.
    - _variables_: a way to remember values.
5. Then write the CSS taking time to explain the `vw` and `vh` units, `justify-items`, `align-items` and the use of `1fr` as a grid unit.

**Extension:**

1. (Easy) Change the images used in the gallery.
2. (Medium) Control the movement of images using a forwards/backwards button.
3. (Hard) Display a visual indicator of the number of images and the current one being displayed.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flowers</title>
        <link rel="stylesheet" href="gallery.css" />
    </head>
    <body>
        <h1>Flower Gallery</h1>
        <img src="flower-2.jpg" id="flower-gallery" />
        <script src="gallery.js"></script>
    </body>
</html>
```

```css
body {
    display: grid;
    height: 100vh;
    width: 100vw;
    grid-template-columns: 100%;
    grid-template-rows: auto 1fr 1em;
    margin: 0;
    justify-items: center;
    align-items: center;
}

h1 {
    text-align: center;
    transition: all 500ms linear;
}

img {
    max-width: 100%;
    max-height: 100%;
    overflow: auto;
    padding: 1em;
}
```
```js
/**
 * Turn an <img> element into a gallery that cycles through the given images on
 * a particular interval.
 * @param {HTMLImageElement} imgElement The <img> element to turn into a gallery.
 * @param {Array<string>} imgUrls The urls of the images to display.
 * @param {number} imgDuration The milliseconds to display each image for.
 */
function createImageGallery(imgElement, imgUrls, imgDuration) {
    let currentPhotoIndex = 0;
    
    /**
     * This function when invoked will cause the next image to display in the carousel.
     */
    function changePhoto() {
        imgElement.src = imgUrls[currentPhotoIndex++ % imgUrls.length];
    }
    
    setInterval(changePhoto, imgDuration);
}

const flowerGallery = document.querySelector("#flower-gallery");
const flowerUrls = [
    "flower-1.jpg",
    "flower-2.jpg",
    "flower-3.jpg"
];
const flowerDuration = 1000;
createImageGallery(flowerGallery, flowerUrls, flowerDuration);
```

## Quizziz Quiz (15min)

Start the quizziz lobby and have students join and complete the quiz (which should take 10min). Then go over the questions students struggled with in the remaining 5min of time allocated for this section.

## Rainbow Text (Pt. 1) (15min)

In this section we'll create a function which allows us to _rainbowify_ an elements text on an interval. Complete by following these steps:

1. Search "MDN random" into google and show the reference page, explain that we'll be copy/pasting their random function to use in our site. Explain that almost all software builds on other software and this is okay to do - but also explain when it isn't appropriate.
2. Create the `rainbowifyElement` function, make sure to explain what **RGB** is by opening up _paint_ and showing the RGB values of various colors.

```js
/* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random */
function random(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function rainbowifyElement(element, colorDuration) {
    function changeColor() {
        const r = random(0, 255);
        const g = random(0, 255);
        const b = random(0, 255);
        element.style.color = `rgb(${r}, ${g}, ${b})`;
    }

    setInterval(changeColor, colorDuration);
}

const galleryHeader = document.querySelector("h1");
rainbowifyElement(galleryHeader, 200);
```

**Extension:**

1. (Easy) Randomly change other properties besides color.
2. (Hard) Create another function called `rainbowifyElementsByQuerySelector` which takes a query selector string as a parameter like `document.querySelector` and applies the rainbow effect to all matching elements.

## Rainbow Text (Pt. 2) (10min)

In this section we enhance our rainbow header to smoothly transition between colors and also change it's size.


```js
element.style.fontSize = `${random(1, 6)}em`;
```
```css
h1 { transition: color 500ms linear, font-size 500ms linear; }
```

**Extension:**

1. (Medium/Hard) Make it so that any element with a "rainbow-text" class will automatically have its text ranbowyfied.

## Dice (20min)

In this section we'll create a dice rolling site by doing the following:

1. Students copy the `dice.html` and `dice.css` file from the shared drive.
2. Copy the `random` function from `gallery.js` into the `<script>` tag.
3. Create a `choose` function, introduce the idea of arrays as a sequence of boxes which you can store things in.
4. Introduce the notion of the DOM event model and that we can listen to these events and respond.
5. Add a _click_ event listener which changes the `src` of the dice `<img>`.
6. Add the CSS to position the button and dice image nicely.
7. Add the shake animation to the dice, explaining that again we've used someone else's code in our program and that it's okay.

```js
function choose(array) {
    return array[random(0, array.length)];
}

const diceImg = document.getElementById("dice");
const rollBtn = document.getElementById("role-btn");

rollBtn.addEventListener("click", () => {
    diceImg.style.animation = "shake 0.5s";
    diceImg.src = choose(FACES);
    setTimeout(() => {
    diceImg.style.animation = "";
    }, 500);
});
```
```css
body {
    display: grid;
    justify-items: center;
    gap: 1em;
}

#dice {
    width: 100px;
    height: 100px;
}
```

**Extension:**

1. (Easy) Show a message to accompany your roll (e.g "That's a low roll!").
2. (Medium) Have several dice which roll when you press the roll button.
3. (Medium) Show a history of your dice rolls.

## Memory Game Integration (35min)

In this section students will attempt to integrate the `memory.css` and `memory.js` files into their site and have the game appear. Students are then given time to experiment with the CSS/JS.

# Focus Questions

N/A


<style>
    article {
        max-width: initial !important;
    }
</style>