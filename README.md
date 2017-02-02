# Sunburst application

## Inspiration
Imaging interpretation for disease progression requires appropriate understanding of prior imaging context, which is typically done by manually examining prior exam reports and images which can be time-consuming and tedious.  Patient timeline tools already exist to provide some of this context, but still require radiologists to review the same data. This motivated me and my team to design and develop an application - Sunburst 

## What it does
Sunburst is capable of summarizing past radiology reports (priors) of patients and presenting the key findings from patients’ clinical history using natural language processing  

## How I built it
I used Metamap (a tool for annotating medical text) and Django web framework to build a parser at the backend. I then pushed the results of parser to front-end for data visualization which was powered using React JS and D3.js. 

## Challenges I ran into
Technical challenges involved making a seamless connection between results produced by Metamap and parser written in python. Non-technical challenges involved understanding medical terms, understand the requirements of radiologists and convert those requirements into features in the product.  

## Accomplishments that I'm proud of
Application developed aims at enabling 50+ clinicians at Weill Cornell Imaging in obtaining a quick snapshot view of patients’ past medical condition thereby reducing the backlog of processing other patient’s reports. Application designed was selected for presentation in one of the world’s largest annual medical conference Radiology Society of North America (RSNA) 2016.

## What I learned
I was new to whole front-end side of this application. I learnt D3.js and React JS from scratch for this project. 

## What's next for Sunburst
Sunburst being an open source project can be further enhanced with prediction capabilities, for example - predicting imaging findings to further enhance workflow and provide additional triage.

## Demo : [http://shuklaham.github.io/visualize-priors/](http://shuklaham.github.io/visualize-priors/)


![Alt text](sunburst_app.png?raw=true "Sunburst App")
