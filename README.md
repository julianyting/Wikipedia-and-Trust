# Trust in Wikipedia

## Group Members

1. Rhea John
2. Imara Zepeda
3. Julia Nguyen
4. AB Owusu-Agyemang
5. Julian Ting
6. Jack Flanagan

## Literature Review

[Research Articles](https://github.com/awohoa/Wikipedia-and-Trust/blob/main/literature-review.md)

## Abstract

In the new world of AI and technology, many wonder how reliable internet sources are. This includes one of the most popular sources of information, Wikipedia. Wikipedia remains relevant and trustworthy partly because it relies on humans who add content by posting and editing contributions on talk pages. However, AI may weaken this reliance on Wikipedia, as large language models can pull answers from Wikipedia and other sources so quickly that users have less need to engage and interact on Wikipedia pages. Our project explores how Wikipedia sustains its trust and relevance in the age of AI, and what its role may look like in the coming years.

## Research Questions

1. How does Wikipedia sustain trust in its content despite being open for anyone to edit?  
   Features like citations, page protection, and talk pages all help. Unlike AI tools, Wikipedia makes the editing process visible—users can see who contributed, when changes happened, and why.
2. In what ways does Wikipedia still have advantages over AI-generated content?  
   Transparency: users can check edit histories, see talk page debates, and review citations.
   Accountability: edits are often tied to specific contributors.
   These features give Wikipedia a level of credibility that AI doesn't because wikipedia articles have citations and discussion which AI doesn't have or often times their citations or links are broken/incorrect.
3. How might Wikipedia adapt in the AI era to remain sustainable and trustworthy?  
   It could use AI as a tool—for example, to help flag unreliable sources or suggest citations. At the same time, it could highlight its human-centered editing model, showing how real people debate, collaborate, and verify information.
4. Why are human contributors still so important for Wikipedia?  
   Without regular users checking and updating content, Wikipedia could lose accuracy and relevance. The platform might need new strategies (like recognition programs or partnerships with schools) to keep people motivated to contribute.



## Methodology

1. We will design a short survey for our classmates (who actively post on Wikipedia) to ask whether and how they use AI tools when writing or editing content. The survey will also ask about perceptions of Wikipedia’s trustworthiness compared to AI tools. This will provide insight into how contributors themselves see the role of AI in the editing process.
2. We will ask Chatgpt questions about the same topics as the selected Wikipedia articles of our choice. We will then compare LLM responses with Wikipedia’s current content to examine overlap, accuracy, and differences.
3. Finally, we will compare our findings with prior research on Wikipedia governance, online trust, and AI’s impact on collaborative knowledge production.


## The Prototype Description

The prototype finds a random Wikipedia article and returns its name, the amount of sources it has, and the amount of revisions it had. It then outputs the text in HTML format of the article.

ADD sentiment analysis, find question that fits program


## Research Question Week 7
Question: Does the number of revisions to an article make an article more trustworthy?

#### Methodology
Use the Wikipedia API to retrieve the revision history for a set of articles.
Record the total number of revisions for each article.
Collect additional metadata such as:
- Article length (in bytes or word count)
- Number of unique contributors
- Date of creation and most recent update
Compare the revision counts with existing Wikipedia quality or trust indicators, such as featured or good article status (available through API properties).
Analyze whether articles with more revisions tend to be higher quality or more trustworthy, based on these indicators.


## Explain how you are going to use the results of the program to answer your question
Our program will collect and analyze data from random Wikipedia articles using the Wikipedia API. Specifically, it will retrieve the number of revisions, the number of sources, and the HTML text of each article. This data will help us evaluate whether a higher number of revisions correlates with greater article trustworthiness.
Revision Analysis:  
We will record how many revisions each article has.
Articles with frequent revisions may indicate active engagement by the community, suggesting that the information is regularly checked and updated.
Combining the Data:  
By combining revision counts, source counts, and sentiment results, we can identify patterns such as:
Articles with more revisions and balanced sentiment being more trustworthy.
Articles with fewer sources or polarized sentiment being less reliable or more controversial.
Answering the Research Question:  
If our analysis shows that highly revised articles align with Wikipedia’s top-rated quality categories and contain balanced or neutral sentiment, it would support the idea that active community editing improves reliability. Conversely, if more revisions are found on low-quality or highly polarized pages, it may suggest that frequent editing alone doesn’t guarantee trustworthiness.
