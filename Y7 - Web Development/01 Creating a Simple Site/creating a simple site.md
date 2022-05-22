
# Creating a Simple Site

In this lesson students are guided by direct instruction to produce a simple web page with minor variation. The focus of the lesson is for students to learn how to work with HTML files using VS Code and a browser, and learn some different HTML elements and how to write them.

## Learning Goals

1. Students can create a HTML file in VS Code and save it with the correct file extension.
2. Students can differentiate between file content and filename.
3. Students can add a _title_ to a web page.
4. Students can create _headers_ and know their sizing.
5. Students can create an _ordered list_ and create a variable number of _list items_ in a list.
6. Students can create _pragraphs_ and use the _em_ and _strong_ tags to change the style of text.
7. Students can create simple _tables_ using _header_ and _data_ cells as appropriate.
8. Students can create simple _forms_ which involve text _inputs_, _textareas_, and _select_ dropdowns.
9. Students can add _images_ to a page.
10. Students demonstrate the ability to correctly write HTML using the aforementioned elements. This includes ensuring all tags are closed and nested appropriately.

## Assessment Plan

1. After explaining the different between file content and filename the following questions will be asked to the class to check for understanding:
   1. How does the computer decide with which program to open a file?
   2. If I created a Word document and wanted it to be a PowerPoint instead, could I just rename the file from "Example.docx" to "Example.pptx"?
2. Periodically when students are working on the 'design' portion of each sub-activity, I will assess how they're going my walking around the class and seeing their work.

## Materials and Resources

1. All students have VS Code installed.

## Teaching Strategies

1. Direct instruction.

## Learning Experience

### Part 1

- (5min) Introduce the lesson by doing the following:
  - For class B ask if anyone completed the MDN activity, if so ask how they found it / what they wrote about.
  - Outline behavioral expectations:
    - When I am addressing the whole class, I need everybody's attention and since I don't like raising my voice I would appreciate it if everyone stopped what they are doing and look towards the front when I say "3, 2, 1, eyes on me".
    - I want you to be working on the same task as we are, I trust that you will do this since I cannot see everyone's screens while I'm at the front.
- (5min) Ensure everyone has VS Code installed
- (2min) Demonstrate how to open VS Code and create a blank HTML file. Ask for a raise of hands for who was able to open VS Code and create the blank file.
- (2min) Show the students how to save the file to their OneDrive. Have them create a folder called "sitebook" and place their file inside it.
- (3min) Explain the difference between file content and the file name and ask the questions outlined in the assessment plan.
- (3min) Walk through the layout of Visual Studio code introducing the following:
  - The file explorer
  - The editor
  - Tabs along the editor
  - How to tell what mode the editor is in
  - Line numbers
  - How to tell if a file has changes that haven't been saved.
- (1min) Have them use the "html" snippet generator to produce the HTML boilerplate.
- (2min) Have students save the file and show them how to open the HTML file.
  - Explain that they simply need to press "refresh" for the browser to reflect their file changes rather than closing and reopening.
  - Show the side-by-side workflow.
- (25min, 21min alloc.) Walk students through the following mini-activities

|Learning|Explanation|Recitation|Variation|
|---|---|---|---|
|Titles (2min)|Show a browser tab and explain how it gets its name from the `<title>` tag.|Demonstrate how to create a `<title>` tag.|Have students change the content of the title and refresh their browser|
|Headers (3min)|Headers are ways of delimiting sections of content and are created with `<h1>`, ..., `<h6>` elements.|Show how to create a `<h1>` and a `<h2>` element.|Students create a header of all six levels by copy-pasting code. They observe the differences in their browser.|
|Paragraphs (3min)|Used to represent text that should display as a paragraph. Useful for compartmentalizing the text of a webpage.|Demonstrate creating a `<p>` and writing content within it.|Have students alter the text in the current paragraph and also create another paragraph.|
|Emphasis (3min)|The `<em>` element is used to place emphasis on a fragment of text. It effects how screen readers work, and visually italicizes text.|Demonstrate the adding of emphasis to a word in one the the previously created paragraphs.|Students add emphasis to their paragraphs as appropriate.|
|Strong (2min)|The `<strong>` element works in the same way as the `<em>` but boldens and draws attention to the text instead.|-|Have students make some text in their paragraph emboldened by using the `<strong>` element|
|Ordered Lists (5min)|The `<ol>` element is used to created an ordered list along with the `<li>` element. For example a list of games ordered by their rating or a leader board.|Re-demonstrate creating a `<h1>` with the content "Tallest Buildings", and add the first 3 entries: "Burj Khalifa, Dubai, 828m", "Shanghai Tower, Shanghai, 632m", "Mecca, Saudi Arabia, 601m".|Students then add the next 2 entries by using the Wikipedia list of tallest buildings.|
|Recap (3min)|-|Suggest that the formatting of our list with the building data is a bit hard to read, perhaps we should use our `<em>` and `<strong>` elements to alter the appearance of either the city or the building height.|Students use the `<em>` and `<strong>` elements to alter the list.

- (6min, if not a double period) Pack up and have them stay until the bell, walk around talking and getting to know students. How did they find the lesson? Did they prefer it to the first one?

### Part 2

- (5min) Revise the previous parts content by asking the following questions to the class:
  - Write the following elements vertically along one side of the board: `<title>`, `<p>`, `<h1>`, `<h6>`, `<ol>`, `<li>`, `<strong>` and `<em>`. Then along the other side of the board enumerate the following options: the text of the tab, a paragraph, the largest header, the smallest header, a list, an item in a list, bold, italic. For each element type go through the options and have the whole class raise their hands to indicate which one they agree with.
  - Should our visible content be placed in the `<head>` or the `<body>` tag? Again hands up.
- (1min) Explain that we'll be exploring some more elements in this lesson.
- (40min, 35min alloc.) Walk students through the following mini-activities

|Learning|Explanation|Recitation|Variation|
|---|---|---|---|
|Tables (10m)|The `<table>` element is used to layout tabular data on a webpage in an accessible format. If we were to re-create a table with other elements it would be very tedious.|Demonstrate the creation of a `<table>` whose columns and content describe the different elements used to create a table.|Students then create another table for a subject of their choice, but it must have at least 3 columns.|
|Forms (10m)|Forms are used to allow users to enter information into a page in a standard way. Web browsers provide functions which can help us process this data. However, forms are not the only way to get user input on a page.|Create a form for ordering a sandwich, use `<select>` for bread type, checkboxes for different condiments/salad, a text input for the name, and a time selector for when the sandwich should arrive, and a textarea for additional instructions. See the HTML snippet below for the code.|Students then add another option to a select, a checkbox, or an additional field.|

<br />

```html
<head>
    <style>
        .field {
            margin: 0.5em;
        }

        legend {
            background-color: cyan;
            padding: 0.2em;
        }

        fieldset {
            border-color: blue;
            background-color: lightgray;
        }

        fieldset:not(:first-of-type) {
            margin-top: 1em;
        }
    </style>
</head>
<body>
    <form>
        <fieldset>
            <legend>Customer Details</legend>
            <div class="field">
              <label for="student-name">Student Name:</label>
              <input name="student-name" type="text">
            </div>
            <div class="field">
              <label for="delivery-location">Delivery Location:</label>
              <input name="delivery-location" type="text">
            </div>
        </fieldset>
        <fieldset>
            <legend>Sandwich</legend>
            <div class="field">
              <label for="filling">Filling:</label>
              <select name="filling" list="fillings">
                  <option>Peanut Butter</option>
                  <option>Beef</option>
                  <option>Beef w/ Salad</option>
                  <option>Cheese</option>
              </select>
            </div>
            <div class="field">
              <label for="bread">Bread:</label>
              <select name="bread" list="bread-types">
                  <option>White</option>
                  <option>Wholemeal</option>
                  <option>Multigrain</option>
                  <option>Gluten Free</option>
              </select>
            </div>
        </fieldset>
    </form>
</body>
```

|Learning|Explanation|Recitation|Variation|
|---|---|---|---|
|Anchors (5m)|`<a>` elements are used to create links between pages. Without anchors we would rely on complex JavaScript to transition between pages.|Create a new HTML file and write into it some content. Then create an anchor tag on the existing page to link to the new page.|Have students add a link to the new page which takes you back to the existing one.|
|Images (10m)|`<img>` elements are used to embed an image inside a page.|Download the images of the tallest buildings alongside the HTML files. Invite a student to come up and add a new *column* to the table. Then after the column is added demonstrate how to add an image for one building.|Have students download the images for the other 4 buildings and create an image for each row.

- (4min) Show students the scratchpad tool they can use to try stuff out if they would like, have them bookmark the GitHub repository.

## Self-Reflection

I felt this lesson went amazingly compared the the previous two. I was very happy when a student said to me that it was a great lesson as he was leaving. I think by using direct instruction as Thomas suggested (and I saw Walter demonstrate) it was easy for students to be engaged and have work to do. It also allowed me to feel more confident as the instruction was very straight forward and relied on my knowledge of the subject. I was pleased when students engaged strongly with my 'match the quiz items' activity, with several students raising their hand to answer each stage at once.

A bit over halfway through the double period I realized that I should probably give the students a break however I didn't manage it very well. Only telling students to come back in 4min after some had already left - it just didn't occur to me! I also should have counted how many returned to ensure nobody was lost however I didn't do this also.

The end of the lesson was a little rushed and I could have perhaps pushed back what I did then to the beginning of next lesson and had a better wrap-up and discussion with the kids.

## Mentor Evaluation

Setup:

Gave direction to students who setup their desks too close.

Much clearer instruction for setup of response to roll. They were still on their laptops, are you okay with this? Would this be an issue in another type of teaching environment?

Reflection questions

Does the setup take as long as you think it will? It was 11:02 when the roll finished. What time did the lesson start. – this is just to give you a rough guide for how to pace your lessons.

Count students when recommencing from a break to ensure you have them all.

Checking for homework?

You can instruct them to open the file they worked on and minimise it and instruct them that you will check when you come round later. This way you set expectations and get a sense of if they have done it or not for real.

Checking for software installed?

Instruction:

Instruction clear: remember to contextualise and give examples prior so students can self-check.

When asking a question, always instruct them how to respond.

When getting a student to assist, instruct them to follow and assist the student by reading out what the student is typing – this ensures information is distributed – but allows you to eye the class and ensure they are following along as well.

Don’t ask for attention – instruct them as you had been doing before.

Behaviour management:

When setting expectations, get them to close their laptops.

Quiz:

When you started did you set them up? Have you written them in the same order as the answer?

Great interactivity with the class but were they all engaged and contributing to the activity. How could you get their attention and engage them all?

Withitness:

Who are your “problem kids” what do problem kids look like?

Had a student come in late. Did you notice them? What instruction could you give them to catch up without stopping the lesson?

When asking students to come back in, remain in a position where you can see everyone?

Some students bailed without packing up – chat to them next time.

Positives:

Instruction greatly improved.

Flow of lesson much better.

Chunking of information much better.

You gave them something to do when you walked around. Very nicely done.

You were not phased when your VS code just started to work just rolled with it.

Energy much better, you clearly know the content and can deliver it well.

Set time limit to the break – maybe also tell them the time and when they should be back as well. Set up what they will be doing when they get back.

Helped students well.

Confidence and student engagement greatly improved.

Lesson timing greatly improved.

To reflect

Your instructions and lesson have meant the students can absorb content quickly, how are you going to accelerate?

General:

A bit rushed towards the end – if it wasn’t necessary for them to have the access to your website next time that way you can go through the routine of ensuring they have it