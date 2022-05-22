# Bubble Sort

Today you will be completing this handout to learn basic Psuedocode. The objective of the handout is to implement the bubble sort algorithim which will sort a list in place. What is a list? What does 'in place' mean? We will find out. At the end of this lesson you <strong>will be submitting a zip file containing your work</strong>.

## What is Bubble Sort?

It is a _sorting_ algorithim. A sorting algorithim takes a collection of items and then orders the items. Consider an incomplete implementation of the bubble sort function below:

```
// Takes a collection of items and sorts them.
Function BubbleSort(Items)
    ...
End Function
```

If we called `BubbleSort` with the list `[5,2,3,1]` we would end up with the sorted list `[1,2,3,5]`. But how does bubble sort work? Here is my brief explanation and a visualization:

Bubble sort works by going over each _pair_ of _neighbouring_ items in a list (the red boxes). If the item on the left is _greater_ than the item on the right, the items swap spots. We repeat this process until we go over the list without swapping the items of any pair.

![bubble-sort-gif](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

Now produce an _ordered sequence of instructions_ which describe how to perform a bubble sort using your own words:

<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Step</th>
        </tr>
    </thead>
    <tbody>
        <tr><td></td><td></td></tr>
        <tr><td></td><td></td></tr>
        <tr><td></td><td></td></tr>
        <tr><td></td><td></td></tr>
        <tr><td></td><td></td></tr>
        <tr><td></td><td></td></tr>
        <tr><td></td><td></td></tr>
        <tr><td></td><td></td></tr> 
    </tbody>
</table>