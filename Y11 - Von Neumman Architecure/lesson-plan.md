# Von Neumman Architecture

## Learning Objectives

- Students can identify the the components of a Von Neumman machine: I/O input, I/O output, memory, CU and ALU.
- Students can explain the fetch-decode-execute cycle with respect to the CI, ALU and memory unit.
- Students can write simple addition and loops for a virtual Von Neumman CPU.
- Students can define primary and secondary memory.

## Activites

- Addition program
- Looping program
- Branching program
- Multiplication program

## Homework

- Students must complete the multiplication program with comments, and provide a paragraph about _why_ the program works.
- Watch this video which discusses the history of Von Neumann https://www.youtube.com/watch?v=Ml3-kVYLNr8

## Sequence

### Part 1

1. [00:10:10] (REVIEW) Review the core concepts discussed in the previous lesson which will be used in this lesson by asking/discussing the following questions (have students discuss with person next to them, then ask the group):
    - What is the abstract definition of a computer?
    - What is the 'FDE' cycle?
    - Where are the instructions for a program stored?
    - What is the purpose of the programme counter?
    - What does 'IR' stand for? What is it used for?
    - What type of value is stored in the accumulator?
    - Lets draw a diagram of a CPU.
2. [10:05:15] Students open up the simulator (http://vnsimulator.altervista.org/) and the following vocabulary is explained with reference to the UI:
    - "memory cell" (these are 'slots' in memory)
    - "variable" (a way of 'naming' a section of memory so it is easier to reffer to)
    - "RAM" (random access memory)
2. [15:05:20] The following UI elements are explained:
    - The UI elements which correspond to the memory, CU, ALU.
    - How to access a guide about the assembly language.
    - How to play / step through execution.
    - How to open samples.
3. [20:15:35] Addition program.
    - [10] Together we complete the shared portion of the 'Addition Program' activity.
    - [02] Students modify the program to **subtract** 5 rather than add 5.
    - [03] Students modify the program to **add** the content of a variable.
4. [35:15:50] Looping program.
    - [5] Together we complete the looping program.
    - [10] Students extend the program so that counds the number of times the program loops.

### Part 2

1. [00:25:25] Branching program.
    - [10] Together we complete the branching program.
    - [15] Students create the 'multiplication program' which accepts two variables `X`, `Y`, and places the product into variable `Z`.
2. [25:05:30] (PPT) The different types of memory are reviewed / prior knowledge activates by discussing RAM, HDD and SSD connection + speed:
    - 20GB/s RAM (plugged into motherboard directly)
    - 200MB/s - 2.75GB/s SSD (SATA cable, or with M.2 directly into motherboard, or via USB externally)
    - 50MB/s - 200MB/s HDD (SATA aka Serial AT Attachment, or via USB externally)
3. [30:05:35] (QUESTION) When editing a word document, or viewing an image on a web page, where is the data for that document or image stored? If the computer suddenly lost power, would the data still be there? Introduce concept of memory volitility, emphasising RAM is volitale, while most storage such as HDD or SSD is non-volitable.
4. [35:05:40] (PPT) Introduce primary memory, it is mostly used to store program data and instructions - it can be directly accessed from the CPU. This is analougus to the 'memory cells' in the simulator. Why might fast **random** access be important for memory which contains our program data?
5. [40:05:45] Discuss CPU cache layers, and the role of RAM and how you can see that whole access pipeline as an optimization layer. If large, non-volitale storage could be _as fast_, and _as durable_ we could probably just reduce these layers. Discuss how when writing high performance code programmers actually take this into account.
6. [45:05:50] (PPT) Discuss how the motherboard other hardware have firmware (intel management engine) 'built into' them in either ROM (READ ONLY) or flash memory which is NOT VOLITALE.
    - Why is it important that the firmware be stored on non-volitale memory?
    - Why is it important that a motherboard's BIOS (basic I/O system) be writable?
    - Where might storing the firmware in ROM be a good idea?
7. [50:05:55] (PPT) Now move onto secondary memory, explain it via contrasting it to secondary memory. Ask what are some examples of secondary memory?


### Addition Program

I write out the different instructions on the board in the format on the altervista website's help section. I then tell them that the following table should produce a program which adds the number 5 to the variable X and places the result in to the variable Y. I then randomly choose students / ask for volunteers to help fill out the program step by step.

|Line|Instruction|Value|Comment|
|--|----|---|------------------|
|0|LOD|?|We want to load the value of variable X into the ALU|
|1|?|#5|We want to add the number 5 to the current value in the ALU, placing the result in the accumulator.|
|2|STO|?|We want to store the result into variable Y|
|3|HLT||?|

Then I, and the students, write these instructions into the simulator and press play. Then I ask them to modify the program in the following ways:

1. It **subtracts** 5 from the number (without writing a negative number!)
2. It **adds** the contents of a variable Z to X instead of a fixed number.

### Looping Program

Together we fill out the following table which should produce a program which contunially increments a number.

|Line|Instruction|Value|Comment|
|--|----|---|------------------|
|0|LOD|?|We want to load the value of variable X into the ALU|
|1|?|?|We want to add the variable Y to the current value in the ALU, placing the result in the accumulator.|
|2|?|?|?|
|3|?|0|We want to jump back to line 0|

Students then modify the program so that it also records the number of times we have incremented X.

### Branching Program

Together we fill out the following table which should produce a program which stores a 1 in Z if the variables X and Y are equal.

|Line|Instruction|Value|Comment|
|--|----|---|------------------|
|0|LOD|X|We want to load the value of variable X into the ALU|
|1|?|?|We want to subtract the variable Y to the current value in the ALU, placing the result in the accumulator.|
|2|JMZ|?|If the accumulator's value is 0 jump to line 6|
|3|LOD|#0|Place the number 0 into the accumulator|
|4|?|?|Store the value of the accumulator into variable Z|
|5|?||Stop the program|
|6|?|#1|Place the number 1 into the accumulator|
|7|?|Z||Place the value of the accumulator into variable Z|
|8|HLT||Stop the program|

Students then make a multiplication program which places the result of `X * Y` into variable `Z`, with the following hint:

|Line|Memory Cell|
|--|----------------|
|0|`// Z = Z + X`|
|1|?|
|2|?|
|3|STO Z|
|4||
|5|`// Y = Y - 1`|
|6|?|
|7|?|
|8|STO Y|
|9||
|10|`// IF Y == 0 THEN: JUMP TO HLT, ELSE: JUMP TO Z = Z + X`|
|11|?|
|12|JMZ ?|
|13|?|
|15|HLT|



## Reflection

...

## Feedback

### 18th May

- give students opporunity to discuss answers to initial questioning with person next to them

### 14th May

- define the variable terminology (recap some terminology I assume they know)
- think of it like a logic puzzle rather than programming
- can draw up a [ ][  ] x rows and partially fill them out, this will help them get started then they can transition to using the simulator
- for the last activity explictly cover multiplcation as repeated edition

### 12th May

- The FDE cycle isn't a syllabus point for year 11 so I wouldn't teach it to a massive degree.
- The task may be too difficult because they don't have much programming skills.

## Code

These are the solutions for the various coding activities.

```asm
// Addition 1
LOD X
ADD #5
STO Y
HLT

// Addition 2
LOD X
ADD Y
STO Z
HLT

// Addition 2
LOD X
ADD Y
STO X
HLT

// Looping 1
LOD X
ADD Y
STO X
JMP 0
HLT

// Looping 2
LOD X
ADD Y
STO X
LOD Z
ADD #1
STO Z
JMP 0
HLT

// Branching Program
LOD X
SUB Y
JMZ 6
LOD #0
STO Z
HLT
LOD #1
STO Z
HLT

// Multiplication
// Z = Z + X
LOD Z
ADD X
STO Z

// Y = Y - 1
LOD Y
SUB #1
STO Y

// IF Y == 0 THEN
//	 EXIT
// ELSE
//	 ADD Y TO Z
LOD Y
JMZ 19
JMP 1

// EXIT
HLT
```
