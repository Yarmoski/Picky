# Picky
A web application that utilizes the Yelp Fusion API to help you decide where to eat.

## How to Use
Go to <insert link> and enter in a location. Picky will provide you with one image at a time. If you want to learn more about the restaurant that the image is from, simply click on the image and the Yelp page will open in a new tab. Click the "Another One!" button to advance to the next image.

## Motivation
Finding a place to eat is ALWAYS a hassle with my friends. They are usually indecisive or refuse to push their preference above others, ultimately resulting in a dialogue that can be boiled down to "You choose!" and "No, you choose!" over and over again. Picky aims to solve this problem by presenting images of food from local restaurants in a fashion similar to the dating app Tinder. After running the idea by some of my friends, I found that there was genuine interest which motivated me to spend hours each day during my winter break working on and learning new information that would help me on Picky. 

## What I learned
While developing Picky, I learned an enourmous amount about web development and the challenges that come with it. I found that I would have had significantly less trouble developing Picky as a local service than as a web application. Working with HTML and CSS, especially CSS, was extremely painful since my prior experience with the two is minimal. However, I am now MUCH more comfortable working with the two and I feel that I can confidently apply HTML/CSS skills to future projects. 

I also learned a great deal about working with APIs through Yelp's Fusion API. I developed what I believe will be a crucial skill in the workplace: learning a new technology/API through quick digestion of its documentation. It was very overwhelming to not have any idea how to use something and be presented with pages and pages of text, many of which did not apply to my specific issue. This feeling was made worse by the lack of outside tutorials and articles on the API. However, it was an amazing rush when things started to click and I got my code to work properly. This came with other learning points such as the best practices regarding API keys and other miscellaneous lessons that I learned along the way.

## Roadmap
The next steps for Picky involve expanding the functionality of its core feature: providing images of local food businesses for the user. This would begin with better location accuracy by taking in the user's exact longitude and latitude either through manual input or other means such as BSSID methods. Yelp's Fusion API supports this, as it allows longitude and latitude parameters in its query interface. 

Another addition regarding search parameters would be check boxes or custom inputs for search terms to provide results specific to the user's current needs. This could be in the form of toggleable areas for categories such as "breakfast" or "casual" as well as custom inputs used for the Yelp query. To add onto this, the ability to specify how many pages or results are returned would also be implemented.

Once these extra QOL features are implemented to Picky, the next obvious step would be to transition to a mobile app. Modern internet usage is transitioning to apps. Additionally, those looking for places to eat are often not at home with access to a desktop computer. While users could technically use their phone's internet browser to access Picky, many are not willing to take the extra steps to do so. An app would provide a convenient and mobile-friendly experience for Picky users.

While the above roadmap features are more practical than the one that follows, I felt like it was worth writing down. It could be benefiical to utilize machine learning to better retrieve more relevant images from Yelp. Yelp's Fusion API provides up to three images that "best represent the business" supposedly chosen by intelligent machine learning algorithms. However, these photos are sometimes not of food, which is the topic of interest, but instead of people or inanimate objects within or surrounding the business. Machine learning could be used to identify pictures of food and only display those on the Picky interface.
