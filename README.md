# Picky
A web application that utilizes the Yelp Fusion API to help you decide what to do. 

## How to Use
Go to [Picky](https://yarmoski.pythonanywhere.com/) and enter in a location. Picky will provide you with one image at a time. 

If you want to learn more about the business that the image is from, simply click on the image and the Yelp page will open in a new tab. Click the "Another One!" button to advance to the next image.

### v2.0 changes
- You can now enter an optional search term. Without a search term, results will be of restaurants and food. Example search terms include boba, lunch, scuba diving, backpacking, electronics, and bakery. Keep in mind that searches for uncommon terms will most likely yield fewer results.
  
### Dev use
Create a directory and store the repo files there. Make sure you have the dependencies (found in requirements.txt) installed in your environment. 
```
git clone https://github.com/Yarmoski/Picky.git
```
Navigate to the directory you created 
```
cd Picky
```
and run the file "Picky.py" to start the development server on default port 5000 (localhost:5000). 
```
python Picky.py
```
Go to 127.0.0.1:5000 (localhost:5000) on your web browser to view the site.

## Motivation
Settling on an activity is ALWAYS a hassle with my friends. They are usually indecisive or refuse to push their preference above others, ultimately resulting in a dialogue that can be boiled down to "You choose!" and "No, you choose!" over and over again. 

Picky aims to solve this problem by presenting food from local restaurants in a fashion similar to the dating app Tinder. Using the power of images, Picky skips the annoying social interaction that comes bundled with deciding what to do.

After running the idea by some of my friends, I found that there was genuine interest which motivated me to spend time working on and learning new information that would help me on Picky. 

I decided to revisit Picky and continue adding more features in anticipation for the burst of activity I expect once the COVID-19 quarantines come out of effect. Picky is a great tool to get back into the public world.

## Roadmap of features
- ~~Non-food attractions mode~~
- ~~Display other stats such as rating, price~~
- ~~Small user-friendliness changes (submit button, loading indicator)~~
- Precise location (long, lat)
- ~~Custom search terms~~
- User-created saved list of businesses per session
- MOBILE APP
- Machine learning food image recognition

### Roadmap Elaborated
The next steps for Picky involve expanding the functionality of its core feature: providing images of local food businesses for the user. This would begin with better location accuracy by taking in the user's exact longitude and latitude either through manual input or other means such as BSSID methods. Yelp's Fusion API supports this, as it allows longitude and latitude parameters in its query interface. 

A "saved list" could be added which would allow users to save restaurants within their session. Once they are done browsing, the user can refer back to the list and review their choices for potential places to eat or bookmark.

Once these extra QOL features are implemented to Picky, the next obvious step would be to transition to a mobile app. Modern internet usage is transitioning to apps. Additionally, those looking for places to eat are often not at home with access to a desktop computer. While users could technically use their phone's internet browser to access Picky, many are not willing to take the extra steps to do so. An app would provide a convenient and mobile-friendly experience for Picky users.

There is also the design choice of whether to preload the Yelp queries before browsing to provide a smoother experience (current design) or to load them incrementally as the user browses. While the former choice would result in less time spent upfront, it would slow down the speed at which the user can scroll through the restaurants. I opted to go for the preload option because I and others that I asked would rather take a slow initial load time for a smoother experience than a fast initial load with a rougher scrolling experience.

It could be beneficial to utilize machine learning to better retrieve more relevant images from Yelp. Yelp's Fusion API provides up to three images that "best represent the business" supposedly chosen by intelligent machine learning algorithms. However, these photos are sometimes not relevant to the business, but instead of people or inanimate objects within or surrounding the business. Machine learning could be used to identify relevant pictures and only display those on the Picky interface.

## What I learned
While developing Picky, I learned an enormous amount about web development and the challenges that come with it. I found that I would have had significantly less trouble developing Picky as a local service than as a web application. Working with HTML, JS, and CSS, especially CSS, was extremely painful since my prior experience was minimal. However, I am now MUCH more comfortable working with the two and I feel that I can confidently apply these skills to future projects. 

Of course, I worked on my core Python skills when developing using Flask and working with Yelp's Fusion API. I cleaned up code and added clarifying comments wherever I could to aid anyone interested in my work. Making Python, JS, HTML, and other web-appy stuff to work together was a hassle and I felt a tangible increase in resolve and grit as I worked through strange issues and vague forum answers to reach solutions to my specific issues.

I also learned a great deal about working with APIs through Yelp's Fusion API. I developed what I believe will be a crucial skill in the workplace: learning a new technology/API through quick digestion of its documentation. It was very overwhelming to not have any idea how to use something and be presented with pages and pages of text, many of which did not apply to my specific issue. This feeling was made worse by the lack of outside tutorials and articles on the API. However, it was an amazing rush when things started to click and I got my code to work properly. This came with other learning points such as the best practices regarding API keys, using environmental variables, managing virtual environments and other miscellaneous lessons that I learned along the way. 

And of course there was the matter of deploying Picky. This was definitely a major obstacle that took hours of research to overcome. I experimented with AWS Elastic Beanstalk and Linux servers, encountered problems with SSH on a Windows machine, read blog posts and tutorials, and also generally floundered around in confusion for a little while. There were extremely strange issues that made absolutely no sense and I don't think I had ever been more frustrated in my life. However, I was able to finally reach a solution that satisfied me resulting in the first deployed version of Picky!
