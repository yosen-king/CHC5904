# Reflective Essay on Analyzing *The Scholars* through Text Mining and Geospatial Visualization

### Introduction

This project is a spatial/textual exploration of 儒林外史 (The Scholars), a classic Chinese novel written during the Qing Dynasty. Using some basic computational methods to analyze the first 10 chapters, I could identify trends in how many times prefectures were mentioned, as well as where the protagonist traveled. It brought together text mining, historiography, and geospatial visualization so that I could use my literary analysis background in combination with methodologies from the growing field of digital humanities. This is a reflection of what was done, the hurdles stepped over and lessons learnt throughout the project.

------

### Methodology Overview

The analysis began by extracting the first ten chapters of *儒林外史* from the Ctext.org platform in their traditional Chinese format. After segmenting the content, I focused on identifying references to specific prefectures shown in the followed table:

| Location | Alias                          |
| -------- | ------------------------------ |
| 南京府   | 金陵府, 建康府, 江寧府         |
| 蘇州府   | 吳郡府, 平江府                 |
| 杭州府   | 臨安府, 錢塘府                 |
| 北京府   | 燕京府, 北平府, 順天府, 大都府 |
| 揚州府   | 廣陵府, 江都府                 |
| 濟南府   | 齊州府, 泉城府                 |
| 湖州府   | 吳興府, 苕溪府                 |

Identifying direct mentions, as well as synonyms, was essential for accurate statistics. I made a frequency count of these prefectures with their synonyms using some Python libraries. To visualize the information, I mapped the results using geopandas along with historical polygon and point data that I acquired from the China Historical GIS (CHGIS). These data were initial coupled using ArcGIS-Python tools, and together a gradient map was produced regarding the frequency of mentions.

After that, I also made use of GPT-4 for semantic analytics to track where in the original story, the character, 匡超人 was traveling (到訪了 曹州府、 杭州府、 湖州府、 江寧府 和 揚州府). Ultimately, this resulted in a path map linking these spots together.



### Key Findings and Interpretation

The analysis yielded several insights. The frequency of mentions across the first ten chapters was as follows: 

| Prefectures | Frequency |
| ----------- | --------- |
| 江寧府      | 2         |
| 杭州府      | 10        |
| 揚州府      | 3         |
| 湖州府      | 8         |

This distribution alludes to the importance of 江南地区 in the narrative corresponding to the cultural and economic significance during the Qing Dynasty. The very high frequency of 杭州府 also agrees with its status as a key cultural hub and a frequently chosen setting in Chinese literature.

From the very beginning of the novel, the journey of 匡超人 through 杭州府, 湖州府, 江寧府, and 揚州府 has been emblematic regarding the thematic concern of travel and examination culture within the book. While mapping his route, it was highly evident that his trajectory was deeply intertwined with the 江南 landscape, reinforcing its role as both the literal and metaphorical stage for the unfolding of personal and societal narratives.



#### Reflections on Geospatial Visualization

The use of geospatial tools really enriched the project. The gradient map visualizing prefecture frequencies provides clarity of the spatial focus of the narrative. Adding CHGIS data ensures it is historically accurate, and the ArcGIS-Python syntax made layering and rendering easy. Adding the path of the journey taken by the protagonist offers an analysis beyond static views of frequency into the dynamics of how the narrative moves spatially.

Choices of visualization told the most in contextualizing data. For instance, 江寧府's low frequency clashes with its symbolic importance: as 南京-the historical capital-it requires reflection on how far the representation of that place is different from the historical reality. Meanwhile, the strong presence of 杭州府 underlined the city's centrality in literature and called for further investigation on how it was represented across Qing literature.



#### Challenges and Insights

The project was not devoid of hurdles. To begin with, the aliases of the prefecture had to be identified with great care owing to the variations in historical and literary usage. As evident from the references of 北京 to 大都-a Yuan Dynasty name-the text manifested temporal layering in a nuanced manner. This consequently made it requisite that historical linguistics be combined with the tools of computational analysis.

Second, the development of the visualization involved a tension between the technical and interpretative. Whereas the geospatial tools allowed for the creation of an accurate mapping, the interpretive work needed to pay attention to historical and literary meaning of the outputs. For example, the visualization of 匡超人's route brought up not only geographic connections but also opened up themes of mobility and social aspiration within the novel.



#### Broader Implications

The value this project demonstrates in digital humanities approaches to the enrichment of literary studies is unparalleled. Merging text mining with geospatial visualization provided an insight into patterns that might be invisible through traditional close reading. Blending historical GIS data into the mix bridged the gap between literary representation and historical geography, offering a multidimensional understanding of *儒林外史*.

The results also show how the 江南 region continued to hold its significance in Qing-era literature. While presenting some of the most important prefectures, *,儒林外史* grasps the socio-economic rhythms of a particular time but also urges the contemporary reader to try to reimagine the contemporary spaces using that historical framework.



#### Conclusion

This reflection underlines the transformative potential of computational methods in literary analysis. The project not only deepened my understanding of *儒林外史* but also expanded my appreciation for the interplay between narrative, geography, and history. It was through the visualization of prefectural focus and the protagonist's journey that new insights came into view related to the novel's spatial dynamics and their wider cultural significance. Thanks to this experience, I continue to dedicate myself to making use of these digital tools in exploring traditional Chinese literature and its many-faceted narratives.






