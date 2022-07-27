# GPT-J-6B For English Quiz Generation
The model was fine-tuned from GPT-J-6B using a set of short and multiple-choice questions from past English quizzes in `training_data`, so that once fed a passage, it can return a quiz of either type. For example, providing the following passage:
<blockquote>
Quantum mechanics developed over many decades, beginning as a set of controversial mathematical explanations for experiments that the mathematics of classical mechanics could not explain, according to the University of St. Andrews in Scotland(opens in new tab). It started at the turn of the 20th century, around the same time 
Albert Einstein published his theory of relativity, a separate revolution in physics that describes the motion of things at high speeds. Unlike relativity, however, the origins of quantum mechanics cannot be attributed to a single scientist. Rather, multiple scientists contributed to a foundation that gradually gained acceptance and experimental verification between the late 1800s and 1930.
</blockquote>

and requesting a short-question, gave us the completion below:

> Question: What did Albert Einstein publish in 1905?\
> Answer: Theory of Relativity.

## Requesting a completion
GPT-J-6B requires immense computational power to load, hence running it on one's PC is not ideal. Using a secret API Key (not provided), one can input a passage and request a model-generated quiz, see `request_demo.ipynb` for example. The seperator `Outline:` at the end of the given passage is necessary for the model to function accordingly.

**URL for request:**

- MC:`https://shared-api.forefront.link/organization/9aDsThyuopVF/gpt-j-6b-vanilla/completions/O5hBBZA60L1h`

- SQ:`https://shared-api.forefront.link/organization/9aDsThyuopVF/gpt-j-6b-vanilla/completions/f3v4Itakh61h`

## Example Output:
|Text    |Completion   |
|--------|---------|
|The fortunes of the empire were thus intimately entwined with those of peoples whose achievements and failures constitute the medieval history of both Europe and Asia. Nor did hostility always characterize the relations between Byzantines and those whom they considered “barbarian.” Even though the Byzantine intellectual firmly believed that civilization ended with the boundaries of his world, he opened it to the barbarian, provided that the latter (with his kin) would accept baptism and render loyalty to the emperor. Thanks to the settlements that resulted from such policies, many a name, seemingly Greek, disguises another of different origin: Slavic, perhaps, or Turkish. Barbarian illiteracy, in consequence, obscures the early generations of more than one family destined to rise to prominence in the empire’s military or civil service. Byzantium was a melting-pot society, characterized during its earlier centuries by a degree of social mobility that belies the stereotype, often applied to it, of an immobile caste-ridden society.|<img width=500/>What might be concluded from this paragraph?<br />A. There were large numbers of immigrants in the ancient Roman Empire.<br />B. The ancient Roman Empire was very tolerant.<br />C. The ancient Roman Empire was the most successful empire in the world.<br />D. The ancient Roman Empire was very wealthy.<br />Answer: B|
|The Industrial Revolution was a period from the 18th to the 19th century where major changes in agriculture, manufacturing, mining, and transport had a profound effect on the socioeconomic and cultural conditions starting in the United Kingdom, then subsequently spreading throughout Europe, North America, and eventually the world. The onset of the Industrial Revolution marked a major turning point in human history; almost every aspect of daily life was eventually influenced in some way. In Europe wild capitalism started to replace the system of mercantilism (today: protectionism) and led to economic growth. The period today is called industrial revolution because the system of Production, production and division of labor enabled the mass production of goods.|<img width=500/>Question: What was different about the society during the Industrial Revolution?<br />Answer: production and division of labor enabled the mass production of goods|
