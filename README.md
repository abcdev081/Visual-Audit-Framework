# Visual-Audit-Framework with Java+Python

## A semi-functional application spell checker framework that detects typographical errors across UI elements.
This project was built to check spelling mistakes that often go unnoticed by humans during testing. It uses Appium (Selenium-based) and tests a native Android app via UIAutomator2. This is only meant to be a skeleton, which needs to be integrated with your app with some work from you or AI.

## What do I do with this skeleton?
![Skeleton actions?](<Skeleton flowchart-1.png>)

## How to install and use this project
1. Clone this project
2. Make sure you have the required dependencies (go through [Dependencies](Dependencies.docx))
3. Refer to the flowchart above. You have two options from here:
    - Option 1: Integrate the skeleton framework directly into your existing app. This option is highly encouraged as it is much more efficient. However, this can only be done if you have prior testing skills to integrate it with your application. Even if you don't, I highly recommend using AI to help you with this. It will ask you for a bunch of xpaths (button locators) that you can use Appium Inspector to get.
    - Option 2: Use the code as it is. It will repeatedly ask you for the depth and multiple xpaths for each button. Make sure to provide the information correctly, or the program may not function as expected
4. For screenshots, you have two options for naming: 
    - Option 1 (default) automatically generates a meaningless name 
    - Option 2 allows you to set a custom name each time a screenshot is taken (set SS_PREFIX_OPTION to True).

5. Start your appium server by writing appium in cmd or using an Appium GUI
6. Run main.py using IntelliJ
> **Note:** No visual spell checker is completely accurate; you can only enhance the image up to a certain extent for your visual engine, after which the picture deteriorates. Do not rely solely on the software—it is meant to assist you, not replace you.

## Known issues
1. Appium is slow
2. Accuracy of the engine is not the best (would keep it at 60-70%)

## How can you contribute?
1. By increasing the accuracy of the engine
2. By making it more modular & universal thus decreasing the LOC

## Dev Note
If you are a QA engineer or have some basic knowledge of testing, you will notice that this is a pretty basic project. However, it is extremely helpful for the general audience. Even with its simplicity, this tool can provide significant value to users who need assistance with visual spell checking.
