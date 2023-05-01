# Coronavirus Twitter Analysis

In this project, a large dataset of tweets was analyzed using MapReduce, a popular parallel processing method for large-scale data. A mapper script was employed to track hashtag usage on both the language and country level. To process the data, a shell script was created to run the mapper script on each file in the dataset. The reduce script was then used to merge the resulting output files. Using the modified visualize script, bar graphs were generated for the top 10 keys in each input file and saved as PNG files. Additionally, an alternative_reduce script was developed to plot the frequency of tweets that used a specific hashtag over the course of a year. Through this project, practical knowledge of data analysis in Python and MapReduce was acquired.

# Language Frequency for #coronavirus
![language_coronavirus](https://user-images.githubusercontent.com/112546626/235536308-33c05181-6a6c-4cb0-8626-ea85ed16c5af.png)

# Language Frequency for #코로나바이러스
![language_korean](https://user-images.githubusercontent.com/112546626/235536330-9d6de6ba-08f3-4290-b716-64b53fd1fba9.png)

# Country Frequency for #coronavirus
![country_coronavirus](https://user-images.githubusercontent.com/112546626/235536341-881b4c15-853a-499b-8375-e0723fb12f28.png)

# Country Frequency for #코로나바이러스
![country_korean](https://user-images.githubusercontent.com/112546626/235536348-dd08265e-565c-4fc1-80ab-7ef20d62b178.png)

# Alternative Reduce Map of #hospital, #flu, and #sick
![sickvhospital_tweet](https://user-images.githubusercontent.com/112546626/235536413-5b73ca01-c21f-4304-8687-567116502a77.png)
