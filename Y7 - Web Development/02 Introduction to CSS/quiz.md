---
title: CSS Quiz
---

As a group work on the following questions - keep in mind the limited time you have! Good luck! For multi-choice just circle the correct answer, if you change your mind just put a slash through the circle.

#### Question 1

For each CSS _selector_ put the number (#) of the _element(s)_ it would match. The first one has been done for you. Note that **not all elements will be matched by a selector!**, and remember a selector can select multiple elements!

:::: columns

::: column

|Selector|Element #s|
|--------|---------------------|
|`th`{.css}|1|
|`em`{.css}||
|`p.red`{.css}||
|`#footer`{.css}||
|`p, a`{.css}||
|`footer`{.css}||

:::

::: column

|#|Element|
|-|----|
|1|`<th>Name</th>`{.html}|
|2|`<footer>(C) Y7 Class</footer>`{.html}|
|3|`<em>go!</em>`{.html}|
|4|`<a class="red" href="site.html">here</a>`{.html}|
|5|`<p>hello world!</p>`{.html}|
|6|`<div id="#footer">(C) 2000 - 2020</div>`{.html}|
|7|`<p class="red">danger</p>`{.html}|

:::

::::

#### Question 2

Given the following HTML

```html
<p class="important">
    We have run out of hashbrowns!
</p>
<p>
    We has run out of avacado.
</p>
```

Write the CSS code below that will do the following:

1. Make the text within any paragraph with an "important" class red AND bold.
2. Make the text size of all paragraphs `15px`;
3. Give all paragraphs a background color of `#a2c`.

<style>
    body {
        ,
    }

    table {
        border-collapse: collapse;
    }

    th, td {
        padding: 0.25em;
        border: 1px solid black;
    }

    .columns {
        display: flex;
        justify-content: space-around;
    }
</style>