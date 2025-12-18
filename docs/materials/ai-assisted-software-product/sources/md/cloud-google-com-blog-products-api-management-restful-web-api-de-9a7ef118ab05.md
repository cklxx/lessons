# RESTful web API Design best practices | Google Cloud Blog

- URL: https://cloud.google.com/blog/products/api-management/restful-web-api-design-best-practices
- Retrieved: 2025-12-18T10:14:18.804271+00:00

API Management
# 
6 common mistakes to avoid in RESTful web API Design
December 1, 2022
  * (https://x.com/intent/tweet?text=6%20common%20mistakes%20to%20avoid%20in%20RESTful%20web%20API%20Design%20@googlecloud&url=https://cloud.google.com/blog/products/api-management/restful-web-api-design-best-practices)
  * (https://www.linkedin.com/shareArticle?mini=true&url=https://cloud.google.com/blog/products/api-management/restful-web-api-design-best-practices&title=6%20common%20mistakes%20to%20avoid%20in%20RESTful%20web%20API%20Design)
  * (https://www.facebook.com/sharer/sharer.php?caption=6%20common%20mistakes%20to%20avoid%20in%20RESTful%20web%20API%20Design&u=https://cloud.google.com/blog/products/api-management/restful-web-api-design-best-practices)
  * (mailto:?subject=6%20common%20mistakes%20to%20avoid%20in%20RESTful%20web%20API%20Design&body=Check%20out%20this%20article%20on%20the%20Cloud%20Blog:%0A%0A6%20common%20mistakes%20to%20avoid%20in%20RESTful%20web%20API%20Design%0A%0AEvery%20modern%20web%20application%20we%20use%20today%20leverages%20APIs%20as%20a%20central%20nervous%20system%20for%20interactions.%20A%20poorly%20designed%20API%20impacts%20developer%20productivity%20and%20application%20performance.%20In%20this%20blog,%20we%20have%20compiled%206%20common%20mistakes%20we%20have%20seen%20in%20API%20design.%0A%0Ahttps://cloud.google.com/blog/products/api-management/restful-web-api-design-best-practices)


##### Varun Krovvidi
Product Marketing Manager, Google Cloud
##### Geir Sjurseth
Outbound Product Manager, Apigee
Imagine ordering a “ready-to-assemble” table online, only to find that the delivery package did not include the assembly instructions. You know what the end product looks like, but have little to no clue how to start assembling the individual pieces to get there. A poorly designed API tends to create a similar experience for a consumer developer. Well designed APIs make it easy for consumer developers to find, explore, access, and use them. In some cases, good quality APIs even spark new ideas and open up new use cases for consumer developers. 
There are methods to [improve API design](https://cloud.google.com/apigee/resources/ebook/web-api-design-register/?int_source=website&int_medium=resources&int_campaign=ebook&int_content=web-api-design-ebook) — like following RESTful practices. But time and again we are seeing customers unknowingly program minor inconveniences into their APIs. To help you avoid these pitfalls, here are six of the most common mistakes we have seen developers make while creating the API — and guidance on how to get it right. 
### #1 Thinking inside-out vs outside-in
Being everything for everybody often means that nothing you do is the best it could be, and that is just as true for APIs. When customers turn to APIs, they are looking for specific solutions to make their work easier and more productive. If there is an API that better works to their needs, they will choose that one over yours. This is why it’s so important to know what your customers need to do their work better, and then building to fill those needs. In other words, start thinking Outside-in as opposed to Inside-Out. Specifically, 
  * **Inside-out** refers to designing APIs around internal systems or services you would like to expose.
  * **Outside-in** refers to designing APIs around customer experiences you want to create. _Read more about the Outside-in perspective in the_[ _API product mindset_](https://cloud.google.com/files/apigee/apigee-api-product-mindset-ebook.pdf) _._


The first step to this is learning from your customers — be it internal consumer developers or external customers — and their use cases. Ask them about the apps they are building, their pain points, and what would help streamline or simplify their development. Write down their most significant use cases and create a sample API response that only gives them the exact data they need for each case. As you test this, look for overlap between payloads and adapt your designs to genericize them across common or similar use cases.
If you can’t connect with your customers — _because you don’t have direct access, they don’t have time, or they just don’t know what they want_ — the best approach is to imagine what you would build with your APIs. Think big and think creatively. While you don't want to design your APIs for vaporware, thinking about the big picture can make it easier to build non-breaking changes in the future. For example the image below showcases [APIs offered by Google Maps](https://mapsplatform.google.com/maps-products/?_gl=1*c81v3b*_ga*MTY4NzQ0NzQyMS4xNjY4ODAzNzQ1*_ga_NRWSTWS78N*MTY2ODgwMzc0NS4xLjAuMTY2ODgwMzc0Ny4wLjAuMA..). Even without diving into the documentation, looking at the names like “Autocomplete” or “Address Validation” clearly outlines the purposes and potential fit for a customer’s use case.
### #2 Making your APIs too complex for users
Customers turn to APIs to bypass complicated programming challenges so they can get to the part they know how to do well. If they feel like using your API means learning a whole new system or language, then it isn’t fitting their needs and they will likely look for something else. It’s up to your team to make an API that is strong and smart enough to do what your customer wants, but also simple enough to hide how complicated the tasks your API solves for really are. For example if you know your customers are using your APIs to present information about recently open restaurants and highly rated pizzeria to their consumers, providing them with a simple API call as below would be of great help:
Loading...
GET /restaurants?location=Austin&category=Pizzeria&open=true&sort=-priority,created_at
To see if your API design is simple enough, pretend you are building the whole system from scratch — or if you have a trusted customer who is willing to help, ask them to test it and report their results. If you can complete the workflow without having to stop to figure something out, then you're good to go. On the other hand, if you catch rough edges caused by trying to code around system complexity issues, then keep trying to refactor. The API will be ready when you can say that nothing is confusing and that it either meets your customers’ needs or can easily be updated as needs change.
### #3 Creating “chatty” APIs with too many calls
Multiple network calls slow down the process and creates higher connection overhead — which means higher operational costs. This is why it’s so important to minimize the number of API calls.
The key to this is outside-in design: simplify. Look for ways to reduce the number of API calls a customer must make in their application's workflow. If your customers are building mobile applications, for example, they often need to minimize their network traffic to reduce battery drain, and requiring a couple calls instead of a dozen can make a big difference. 
Rather than deciding between building distinct, data-driven microservices and streamlining API usage, consider offering both: fine-grained APIs for specific data types, and “experience APIs” _(APIs that are designed to power user experiences. Here is a further_[ _theoretical discussion_](https://www.googlecloudcommunity.com/gc/Apigee/What-is-an-Experience-API-When-should-you-make-one-Isn-t-it/td-p/21080) _on Experience APIs)_ around common or customer-specific user interfaces. These experience APIs compose multiple smaller domains into a single endpoint; making it much simpler for your customers — especially those building user interfaces — to render their screens easily and quickly.
Another option here is to use something like [GraphQL](https://graphql.org/) to allow for this type of customizability. Generally you should avoid building a unique endpoint for every possible screen, but common screens like home pages and user account information can make a world of difference to your API consumers. 
### #4 Not allowing for flexibility
Even if you’ve followed all of the steps above, you may find that there are edge cases that do not fit under your beautifully designed payloads. Maybe your customer needs more data in a single page of results than usual, or the payload has way more data than their app requires. You can’t create a one-size-fits-all solution, but you also don’t want a reputation for building APIs that are limiting. Here are 3 simple options to make your endpoints more flexible. 
  * Filter out response properties: You can either use query parameters for sorting and pagination, or use [GraphQL](https://cloud.google.com/blog/products/api-management/how-to-manage-graphql-apis-in-apigee) which provides these types of details natively. By giving customers the option to request only the properties they need, it guarantees that they won’t have to sort through tons of unnecessary data to get what they need. For example, if some of your customers only need the title, author, and bestseller ranking, give them the ability to retrieve only that data with a query string parameter.


Loading...
GET /books?fields=title,author,ranking
  * Ability to sort with pagination. Generally, you don't want to guarantee the order of objects in an API response because minor changes in logic or peculiarities in your data source might change the sort order at some point. In some cases, however, your customers may want to sort by a particular field. Giving them that option, combined with a pagination option, will give them a highly efficient API when they only want the top few results. For example [Spotify API](https://developer.spotify.com/documentation/web-api/) utilizes a simple offset and limit parameter set to allow pagination. A sample endpoint as shown in the documentation would look like this


Loading...
$ curl https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6/albums?album_type=SINGLE&offset=20&limit=10
  * Use mature compositions like GraphQL: Since customer data needs can differ, giving them on-the-fly composites lets them build to the combinations of data they need, rather than being restricted to a single data type or a pre-set combination of data fields. Using GraphQL can even bypass the need to build experience APIs, but when this isn’t an option, you can use query string parameter options like “expand” to create these more complex queries. Here is a sample response that demonstrates a collection of company resources with embedded properties included


Loading...
"data": [ { "CompanyUid": "27e9cf71-fca4", "name": "ABCCo", "status": "Active", "_embedded": { "organization": { "CompanyUid": "27e9cf71-fca4", "name": "ABCCo", "type": "Company", "taxId": "0123", "city": "Portland", "notes": "" } } } ]
### #5 Making design unreadable to humans 
“K”eep “I”t “S”imply “S”tupid when you are designing your API. While APIs are meant for computer-to-computer interaction, the first client of an API is always a human, and the API contract is the first piece of documentation. Developers are more apt to study your payload design before they dig into your docs. [Observation studies](https://sigdoc.acm.org/cdq/how-developers-use-api-documentation-an-observation-study/) suggest that developers spend more than 51% of their time in editor and client as compared to ~18% on reference. 
For example, if you skim through the payload below it takes some time to understand because instead of property names it includes an “id”. Even the property name “data” does not suggest anything meaningful aside from just being an artifact of the JSON design. A few extra bytes in the payload can save a lot of early confusion and accelerate adoption of your API. Notice how user-ids appearing on the left of the colon (_in the position where other examples of JSON ideally have property names_) creates confusion in reading the payload.
Loading...
"{id-a}": { "data": [ { "AirportCode": "LAX", "AirportName": "Los Angeles", "From": "LAX", "To": "Austin", "departure": "2014-07-15T15:11:25+0000", "arrival": "2014-07-15T16:31:25+0000" } ... // More data ] },
We think that JSON like this is more difficult to learn. If you want to eliminate any ambiguity in the words you choose to describe the data, keep the payload simple and if any of those labels could be interpreted in more than one way, adjust them to be more clear. Here is a sample response from Airlines endpoint of [aviationstack API](https://aviationstack.com/documentation#airlines). Notice how the property names clearly explain the expected result while maintaining a simple JSON structure.
Loading...
"data": [ { "airline_name": "American Airlines", "iata_code": "AA", "iata_prefix_accounting": "1", "icao_code": "AAL", "callsign": "AMERICAN", "type": "scheduled", "status": "active", "fleet_size": "963", "fleet_average_age": "10.9", "date_founded": "1934", "hub_code": "DFW", "country_name": "United States", "country_iso2": "US" }, [...] ]
### #6 Know when you can break the RESTful rules
Being true to the RESTful basics — such as using the correct HTTP verbs, status codes, and stateless resource-based interfaces — can make your customers' lives easier because they don't need to learn an all new lexicon, but remember that the goal is just to help them get their job done. If you put RESTful design first over user experience, then it doesn’t really serve its purpose.
Your goal should be helping your customers be successful with your data, as quickly and easily as possible. Occasionally, that may mean breaking some "rules" of REST to offer simpler and more elegant interfaces. Just be consistent in your design choices across all of your APIs, and be very clear in your documentation about anything that might be peculiar or nonstandard. 
### Conclusion
Beyond these common pitfalls, we have also created a [comprehensive guide](https://cloud.google.com/apigee/resources/ebook/web-api-design-register/?int_source=website&int_medium=resources&int_campaign=ebook&int_content=web-api-design-ebook) packaging up our rich experience designing and managing APIs at incredible scale with Google Cloud's API management product, Apigee. 
Apigee — Google Cloud’s native API management platform — helps you build, manage, and secure APIs — for any use case, scale or environment. Get started with [Apigee](https://cloud.google.com/apigee) today or check out our [documentation](https://cloud.google.com/apigee/docs/api-monitoring) for additional information.
Posted in
  * [API Management](https://cloud.google.com/blog/products/api-management)
  * [Application Modernization](https://cloud.google.com/blog/products/application-modernization)
  * [Application Development](https://cloud.google.com/blog/products/application-development)


##### Related articles
[AI & Machine LearningAnnouncing MCP support in Apigee: Turn existing APIs into secure and governed agentic toolsBy Megan Bruce • 5-minute read](https://cloud.google.com/blog/products/ai-machine-learning/mcp-support-for-apigee)
[API ManagementGoogle Cloud Apigee Named a Leader for the 10th Consecutive Time in the Gartner® Magic Quadrant™ for API ManagementBy Geir Sjurseth • 4-minute read](https://cloud.google.com/blog/products/ai-machine-learning/apigee-a-leader-in-2025-gartner-api-management-magic-quadrant)
[Security & IdentityProtecting your APIs from OWASP’s top 10 security threatsBy Megan Bruce • 11-minute read](https://cloud.google.com/blog/products/identity-security/protecting-your-apis-from-owasps-top-10-security-threats)
[API ManagementOperationalizing generative AI apps with ApigeeBy Michael Vakoc • 7-minute read](https://cloud.google.com/blog/products/api-management/using-apigee-api-management-for-ai)
### Footer Links
#### Follow us
  * (https://www.x.com/googlecloud)
  * (https://www.youtube.com/googlecloud)
  * (https://www.linkedin.com/showcase/google-cloud)
  * (https://www.instagram.com/googlecloud/)
  * (https://www.facebook.com/googlecloud/)


(https://cloud.google.com/ "Google Cloud")
  * [Google Cloud](https://cloud.google.com/)
  * [Google Cloud Products](https://cloud.google.com/products/)
  * [Privacy](https://myaccount.google.com/privacypolicy?hl=en-US)
  * [Terms](https://myaccount.google.com/termsofservice?hl=en-US)
  * [Cookies management controls]


  * [Help](https://support.google.com)
  * Language‪English‬‪Deutsch‬‪Français‬‪한국어‬‪日本語‬
