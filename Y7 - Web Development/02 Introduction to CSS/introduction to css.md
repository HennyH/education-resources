---
title: Introduction to CSS
---

## Learning Goals

1. Students learn that there is a web technology called CSS used to alter the appearance and layout of web pages.
2. Students can provide definitions for the following CSS terms: stylesheet, ruleset, rule, property, value, selector.
3. Students can write simple selectors (element, class, id).
4. Students can use the color, background, font, border, display, margin and padding to style a page.

## Assessment Plan

1. Periodically when students are working on the 'variation' portion of each sub-activity, I will assess how they're going my walking around the class and seeing their work.
2. End of class quiz.
3. Online CSS selector resource.

## Materials and Resources

1. All students have VS Code installed.
2. Example _creating a simple site_ HTML file on GitHub for those that didn't complete the full lesson.

## Teaching Strategies

1. Direct instruction.

## Learning Experience (54min, 45min usable)

- (1min) Tell students we'll be learning how to style the website we made in the previous lesson. This includes being able to do the following:
  - Change the color of text.
  - Change the font type (asked by **Addy**, class A).
  - Add borders to tables.
  - Set background colors.
- (2min) Have students bookmark the project GitHub, show them how to explore the code in the repository and open the site.
- (2min) Ensure everyone has a working copy of the page they created during the _creating a simple site_ two part lesson, if students don't have their own they should copy the contents of the example file from the GitHub.
- (20min) Walk students through the following mini-activities

|Learning|Explanation|Recitation|Variation|Differentiation|
|---|---|---|---|---|
|(4min) `<style>`|The style element is one way to include CSS on our site, the content written between the opening and closing tag is interpreted as CSS.|Create a `<style>` element in the header and write a rule of `html { background-color: lightgray; }`. Explain the syntax of this rule after showing the result.|Change the background color of another element on the page, perhaps a paragraph, or a table?|Search up 'hex' color codes and try some more unique colors.|
|(3min) Font Family|The font family is analogous to the 'Font' selection in world. We use it to change the font of an element.|Open up [fonts.google.com](https://fonts.google.com) and show students all the fonts. Explain we'll be using one on our site. Give them 30s to choose their font. I'll use _Press Start 2P_. Show how to embed the font in their website. **Re-iterate how the element selectors work**.|Have students use different fonts on the page by applying different fonts to different elements.|-|
|(7min) Font Properties|The font properties besides `font-family` can be used to change the boldness, italic, color, and size.|Demonstrate how to make the text of the form `<label>` and `<legend>` bigger (introducing the comma operator in CSS selectors) using `font-size`. Make the `<legend>` text **bold** and _italic_ using CSS. Make the `<label>` text a different color using `color`. Also use `text-align: center` to make the text center (h1, h2 too)|Have students spend the remainder of the 7 minutes styling their page.|Ask students to have a go at using a selector that applies to 3 types of elements and if they do this raise their hand and I'll come take a look.|
|(6min) Table Styling|N/A - Done as part of recitation for each component|Style the table using the following selectors/properties (in order): <br /> `th, td { border: 1px solid black; padding: 0.25em; }`, <br /> `table { border-collapse: collapse; }`, <br /> `tbody > tr:nth-child(2n) { background-color: lightgray; }`|Write a selector which colors the **odd** rows a different color.|Make the last row row a different color using a special pseudo-selector.|

- (15min) Students work on the [flukeout.github.io](https://flukeout.github.io/) game to further practice their CSS selectors. Walk students through the first 4 questions. Ask them to spend 10 minutes each day working their way through the site (optional). If they complete all segments they get their names placed on the CSS Selector Wizard list in the classroom.
- (5min) Each table group gets given the end of class quiz to complete. Assign each group a letter to write on their sheet. Mark as students pack up and let them know their score.

## Focus Questions

1. How to we write an element and class CSS selector?
2. What are some CSS properties to edit the appearance of text?
3. How do we set the background color of an element?

<style>
    table {
        overflow: initial !important;
    }

    article {
        max-width: 100% !important;
    }
</style>