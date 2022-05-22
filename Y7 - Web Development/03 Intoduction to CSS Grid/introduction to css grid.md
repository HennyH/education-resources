Learning Goals
==============

1.  Students can create simple fixed and responsive grids to layout
    content on a web page.
2.  Students can create CSS transition animations to change the rotation
    and background color of an element.
3.  Students can create anchor tags to link pages together.

Assessment Plan
===============

1.  Periodically when students are working on the ‘variation’ portion of
    each sub-activity, I will assess how they’re going my walking around
    the class and seeing their work.

Materials and Resources
=======================

1.  The completed HTML file from the previous lesson for those that did
    not complete all the requirements.

Teaching Strategies
===================

1.  Direct instruction.

Learning Experience (54m)
=========================

-   (10min) Overview of what CSS grid is and the problem it solves.
    -   Draw wireframes of some common websites and demonstrate how CSS
        grid can help lay out that content easily, some examples
        include: Facebook, Instagram.
    -   Introduce the following terminology with reference to the
        wireframes:
        -   Grid container
        -   Grid item
        -   Grid cell
        -   Grid area
        -   Grid gap
        -   **Grid lines**
        -   Tracks
-   (41m) Walk students through the following mini-activities:

| Learning             | Explanation                                                                                                                                                                              | Recitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Variation                                                                                                                                           |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| (8m) Tetris          | We’ll be using CSS grid to create some Tetris shapes. The shapes can be found at [en.wikipedia.org/wiki/Tetromino](https://en.wikipedia.org/wiki/Tetromino), keep this open to one side. | First create a `<ul>` to contain our list of tiles. Give it an **id** to practice the **id selector** in CSS when we set the `list-style: none`. Now in the `<li>` add a `<span>` for the name which we’ll style with CSS, then create a `<div>` and use the classname. Next create `<div>`(s) for each tile, giving all of them the `tile` class and also specifying the color. Demonstrate by creating a T shape. Now in the CSS go `.tetromino { display: grid; grid-template-columns: 50px 50px 50px; }`, the tiles also need to be styled with `.tile { border: 1px solid lightslategray; height: 50px; width: 50px; }` then add the `.empty`, `.green`, etc… classes to color the tiles. | Have students add 1-2 more tiles to the list. **Extension:** Have students create a tile for the first letter of their name by adding more columns. |
| (2m) Tetris Refactor | We’re going to learn a nicer way to specify our column widths.                                                                                                                           | Demonstrate how to change the `grid-template-columns` property to use `repeat(3, 50px)`, and then `repeat(3, max-content)` to allow us to more easily change the tile size.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Adjust the size of the tiles and ensure they are displayed correctly.                                                                               |
| (10m) Form Layout    | *Draw on the board* a wireframe for our form and discuss the CSS columns/widths we’ll need.                                                                                              | Then go to the code and on the `fieldset` element use `fieldset { display: grid; grid-template-columns: max-content minmax(200px, 1fr); }`. Introduce the different concepts and demonstrate how we can now adjust the width of the form and it still looks good.                                                                                                                                                                                                                                                                                                                                                                                                                              | N/A                                                                                                                                                 |
| (15m) Navbar         | Navbars are used to display the main navigation options/pages to users.                                                                                                                  | Create a `<nav>` element and populate it with `<a>` tags. Inside of it put text to different pages, for example “Homepage”, “Games”, “Facts”. Suggest using emojis as icons, place the icons in a `<span>` and give it a **classname**. Then walk through applying the following CSSS:                                                                                                                                                                                                                                                                                                                                                                                                         | Edit the color, font, padding, hover styles and animation to suit personal preferences.                                                             |

<div id="cb1" class="sourceCode">

    nav {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
    }

    nav > a {
      text-align: center;
      background-color: lightseagreen;
      padding: 0.25em;
    }

    nav > a:hover {
      color: white;
    }

    nav > a:hover > .nav-icon {
      transform: rotate(360deg) scale(1.5, 1.5);
      transition: all 200ms linear;
    }

    .nav-icon {
      display: inline-block;
    }

</div>

| Learning   | Explanation                                                                          | Recitation                                                                                                           | Variation                                                                          |
|------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| (5m) Links | At the moment the anchor tags do not take you to a different page.                   | Create 2 new HTML files and name them after the tabs. Then change the `href` of the anchors to point to those files. | Have students link to pages they want, and have them put some HTML on those pages. |
| (1m)       | Show students the resources they can use to learn more and the CSS grid garden game. | N/A                                                                                                                  | N/A                                                                                |

Focus Questions
===============

1.  How do we approach using CSS grid to style a page? (Thinking in
    terms of wireframes, columns, rows etc…)
2.  How do we link pages together?
