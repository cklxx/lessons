# Leverage AI for Mock Tables and Charts When Testing Prototypes - NN/G

- URL: https://www.nngroup.com/articles/ai-data-prototype-testing/
- Retrieved: 2025-12-18T10:16:01.180352+00:00

Skip to content
**NEW RESEARCH COURSES: UX Research Methods, Heatmaps | [Learn More](https://www.nngroup.com/news/item/new-courses/)**
Open main navigation [ Nielsen Norman Group ](https://www.nngroup.com/)
  * Training & UX Certification 
    * [All Live Courses](https://www.nngroup.com/courses/)
    * [Live Online Training Events](https://www.nngroup.com/training/live-courses/)
    * [Private Team Training](https://www.nngroup.com/team-training/)
    * [Bulk Discounts](https://www.nngroup.com/training/bulk-discounts/)
    * [UX Certification](https://www.nngroup.com/ux-certification/)
  * [Articles & Videos](https://www.nngroup.com/articles/)
  * [Consulting](https://www.nngroup.com/consulting/)
  * [Reports & Books](https://www.nngroup.com/reports/)
  * About NN/g 
    * [Overview](https://www.nngroup.com/about/)
    * [People](https://www.nngroup.com/people/)
    * [Clients](https://www.nngroup.com/about/about-client-list/)
    * [News](https://www.nngroup.com/news/)
    * [Contact Us](https://www.nngroup.com/about/contact/)


(https://www.nngroup.com/cart/)
Profile 
Search
Search
Reset Search
12
# Leverage AI for Mock Tables and Charts When Testing Prototypes
Evan Sunwall
[ Evan Sunwall](https://www.nngroup.com/articles/author/evan-sunwall/)
September 6, 2024 2024-09-06
[ Share ]
  * [ Email article ](mailto:?subject=NN/g Article: Leverage AI for Mock Tables and Charts When Testing Prototypes&body=https://www.nngroup.com/articles/ai-data-prototype-testing/)
  * [ Share on LinkedIn ](http://www.linkedin.com/shareArticle?mini=true&url=http://www.nngroup.com/articles/ai-data-prototype-testing/&title=Leverage AI for Mock Tables and Charts When Testing Prototypes&source=Nielsen%20Norman%20Group)
  * [ Share on Twitter ](https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/ai-data-prototype-testing/&text=Leverage AI for Mock Tables and Charts When Testing Prototypes&via=nngroup)


Summary:  Creating realistic data for prototypes is a chore. Use these prompting tactics with generative AI to enhance content fidelity in usability testing. 
Prototype testing is at the core user-centered design. But crafting realistic data for prototypes that you plan to test is time-consuming. Especially when the design itself is still evolving, you’re pressed for time, or you are a [one-person UX team](https://www.nngroup.com/training/course/4901/one-person-ux-team/). Don’t let the struggle of crunching numbers discourage you. Generative AI can help.
##  In This Article: 
(#)
  * Users Will Scrutinize Your Tables and Charts
  * Be Cautious with Your Real Data
  * Craft a Promptframe
  * 7 Tactics for Generating Mock Tables with AI
  * 7 Tactics for Generating Mock Charts with AI
  * Importing Tables into Design Tools
  * Differences in AI Tools for Mock-Data Generation
  * Opportunities with Synthetic Data in Regulated Industries


## Users Will Scrutinize Your Tables and Charts
Research in data sensemaking by Laura Koesten and colleagues found that when participants were given unfamiliar data, they spent more time looking for outliers and inconsistencies than when they worked with familiar data. If you plan to test a prototype (especially if your [user personas](https://www.nngroup.com/articles/persona/) critique data frequently), **your study participants will scrutinize the prototype’s tables and charts, whether you want them to or not**.
This article will discuss practical tactics that any UX professional with access to a general-purpose generative AI tool can use to create higher-quality charts and tables efficiently. To illustrate these tactics, we use a hypothetical example of a sales and marketing-management app targeting ecommerce retailers.
## Be Cautious with Your Real Data
Some of the tactics I recommend involve sharing portions of actual data or examples. In any situation involving generative AI (genAI) and your organization’s data, always be informed and follow your organization’s policies and data-protection regulations.
We recommend that you never share sensitive or identifying data with genAI tools unless your company has verified and approved their use.
## Craft a Promptframe
Start by gathering the information needed to inform your mock-data generation. Create a [promptframe](https://www.nngroup.com/articles/promptframes/) to establish objectives and requirements for content areas. This hybrid form of prompt writing and wireframes will help you facilitate dialog with your collaborators and build prompts to use with an AI.
During this process, remember your testing goals and usability-testing tasks. What would you hope users will accomplish with the prototype during testing? Where are the contentious parts of the design that need clarification?
## 7 Tactics for Generating Mock Tables with AI
Consider these 7 tactics when crafting the prompt for generating tables.
### 1\. Contextualize Tables to Your Audience
**Consider the contextual qualities that the AI should mimic** and reference from its training data. Your table will be less helpful if your AI is modeling data for a large enterprise when your app targets mall businesses. For example, business size, industry or market, geography, or time periods can all influence the table’s data.
In addition, ask yourself whether the AI should use real or just realistic names for data such as companies or products. Include these details in the prompt.
_Claude 3.5 Sonnet was prompted to demonstrate two scenarios of how context affects the generated data. Scenario 1 was focused on data suitable for a large athletic-shoe corporation in the United States. It used real shoe names and large sales volumes. Scenario 2 was focused on data for a boutique shoemaker in France. It had tiny sales volumes, high prices in euros, and French-styled shoe types._
### 2\. Define Volume
**Determine how much data needs to be generated.** You may have room to display only a few dozen rows of a data table in your prototype, but the dataset may be much larger. Describe the size of the larger dataset, if known, so the AI can account for these additional records when calculating values. Mention that you require only a subset to be generated.
For example, a table may typically contain approximately 2,000 transactions totaling 7 million dollars of revenue. You only need 50 transactions to show in your prototype. The AI will account for 2,000 transactions when generating revenue values for those 50.
_Claude 3.5 Sonnet was prompted to demonstrate two scenarios illustrating the impact of defining volume on generated data. In both scenarios, Claude was prompted to generate daily revenue for 10 shoe products, assuming $10 million in total annual revenue. Scenario 1’s prompt did not mention how many shoe products the company sold. Scenario 2’s prompt mentioned that the company sold 100 different shoe products. Scenario 2’s revenue numbers were much smaller compared to Scenario 1, since Claude factored in revenue from 90 other products._
### 3\. Apply Sorting
Ask yourself if **there is an ideal ordering for the data.** There is no need for you to sort your table manually in a spreadsheet; instruct the AI to sort the data by that value.
### 4\. Provide Specifications for the Data
Add these specifications to your prompt for more authentic-looking data for your table.
  * **Uniqueness** : Do all **the values need to be distinct, or can there be duplicates**? For example, a _Product_ _Name_ , _Tracking Number_ , or _Email Address_ column would typically not contain duplicate values.
  * **Fixed values** : Sometimes, **data has predefined values** that must be used. Enumerate those options in your prompt. For example, each row's _Status_ column can be tagged only as _Open_ , _In Progress_ , or _Closed_.
  * **Formatting** : Specify the format you need in your prompt, such as _DD MM YYYY_ for dates or $XX.99 for prices. (A common pricing tactic is to have product prices end in .99, such as $19.99.)
  * **Plausible ranges** : Determine a **realistic range to bound** values in the table. For example, average product ratings on ecommerce sites typically range from 1 to 5 stars, or human systolic blood pressure generally ranges from 90 to 140 mmHg.
  * **Flexible and inflexible constraints** : If there is data where it does not matter what the generated values are, **make it clear to the AI that it can adjust those values** to comply with other constraints you’re placing on the table. But mention any specific values that your usability-testing task and prototype design depend on. For example, if a usability-testing task depends on the fact that product named _Roadrunner Sprinter_ has the most customer complaints, then mention that as a requirement in your prompt.
  * **Value distribution** : Sometimes, you want values to be over- or underrepresented in the table. For example, a table listing code defects that developers must fix may have few rows with an _In Progress_ status. **Mention these useful distribution types in your prompt** to guide the AI in distributing values: 
    * **Normal distribution** : This is the classic bell curve. Most values center around the mean, with a minority at the extremes.
    * **[Pareto](https://www.nngroup.com/articles/pareto-principle/) distribution**: A few data points generate most of the impact, while most others generate little. For example, it’s common for only a few products to generate most of a company’s sales.
    * **Uniform distribution** : Values are spread evenly across a range of potential values.
    * **Custom distribution** : Mention precisely how you want the values distributed. For example, 20% of rows should use _Value A_ , 60% should use _Value B_ , 20% should be blank, and so on.


### 5\. Provide a Chart and Generate Supporting Data
If you have a specific chart already designed but need the tests participant to also be able to inspect the table containing that chart’s data, **upload the chart along with your prompt**. Thanks to the multimodal capabilities of today’s AI tools, they can use this added context when generating table data.
_Claude 3.5 Sonnet was provided with a bar-chart image and prompted to generate transaction data for the worst-performing product. The worst-performing product and the exact sale values were unspecified in both the bar chart and the prompt to test Claude’s multimodal capabilities. Claude correctly identified the worst-performing product, estimated a reasonable value from the bar chart, and generated the table._
### 6\. Contextualize Tables to Your Participants
Leverage AI’s abilities to quickly regenerate and revise data to create mock tables tailored to your users.Ask yourself: What do you know about your usability-testing participants? What kinds of data do they use in their domain, and how would that affect the test of your design? For example, a prototype focusing on shoe products could be pivoted into hats with minimal change.
Share your existing mock table with the AI and ask it to revise it with a description of the participant’s background and context. Then, reupload that table back into the prototype.
### 7\. Require Explicit Calculations and Verification
Always **be cautious when dealing with numbers and generative AI**. Large language models’ math skills depend on help from additional tools. Sometimes, the AI will rely on patterns found in its training data, which may fail in more complex calculations. Worse, the AI will confidently hallucinate that it diligently followed your instructions when it did not. Therefore, use these approaches in your prompts to avoid errors:
  * **Prompt for using coding tools** : Confirm that your AI can use coding tools (namely Python, which is well-suited for math) and require their use for all numerical calculations. You should also check the AI tool's interface to see if the AI indeed generated and executed code for numerical values (even if you don’t know Python).
  * **Ask for explicit calculations** : Ask that the AI show its work when performing calculations. For example, the prompt may say "Sum the _Revenue_ column and show your calculation process."
  * **Require verification** : Instruct it to doublecheck each result according to your requirements before completing its task. For example, "Verify that the _Revenue_ column totals exactly $487,455 before finishing your task.”


You may need to display totals in other parts of your prototype, so requesting them in your prompt makes you more efficient and the AI more accurate in its mock-data generation.
_Claude 3.5 Sonnet was prompted to generate a mock table of athletic-shoe products with various requirements and a total revenue of approximately $487,455. Since Claude was prompted to show calculations and verify its work, it met most requirements but overshot the desired total revenue. Claude self-corrected and eventually provided a dataset that complied with the desired total revenue. That said, a more reliable method would have been for Claude to use Python to calculate the total accurately, but this version of Claude lacked that capability._
## 7 Tactics for Generating Mock Charts with AI
### 1\. Describe What to Show
Rather than fumbling with numbers for charts, **describe the story** instead. Part of what makes AI powerful is that you can use natural language to convey your intent.
For example, you could include in your prompt that overall revenue has been trending downward over the past year, but there was a spike in December due to seasonal holiday demand. The AI will generate a starting point for your narrative, and you can further refine it.
### 2\. Eliminate the Clutter
The AI tool may render charts with gridlines, drop shadows, or legends that are [**more clutter than**](https://www.nngroup.com/articles/clutter-charts/)**insight**. By default, most AI tools will include some of these chart elements, so ask it in your prompt not to use them.
### 3\. Emphasize Outliers
In many usability-testing tasks, charts can visualize outliers that require user analysis and attention. **In your prompt, call out these outliers.**
For example, in a bar chart depicting sales performance across sales representatives, you might specify that one person, _Sam H.,_ has accomplished roughly only 20% of his sales quota, and only his bar should be shaded red. This instruction would be helpful if you were testing to see if the user notices _Sam H_.’s lagging performance and engages in a sales-coaching workflow.
### 4\. Specify Dimensions
**Include the chart’s dimensions** in your prompt. (You may copy them from your promptframe, if using one.) Setting dimensions will save you significant time readjusting chart elements to fit them into the interface.
### 5\. Request SVG format
Request that generated charts use **the scalable vector graphics (SVG) format**. Compared to image formats (JPEG or PNG), SVG preserves the editability of individual chart elements in design tools, which is important if you need to make small adjustments to the chart later.
_Generating charts in SVG format makes them easy to import and edit in design tools like Figma._
### 6\. Don’t Delegate Critical Thinking
Even though AI can rapidly construct and modify charts, Claude 3.5 Sonnet and ChatGPT 4o would dutifully create nonsense charts, even when prompted to act as a data-visualization expert. These tools have impressive capabilities, but **they need a discerning human prompter**.
You must train on [effective data-visualization techniques](https://www.nngroup.com/articles/choosing-chart-types/) if you frequently design chart content. Relying on AI to catch your mistakes is a mistake.
_ChatGPT4o and Claude 3.5 Sonnet were prompted to act as data-visualization experts and asked to critique this uploaded line chart. Both initially failed to recognize that the chart showed meaningless and misleading product trends. However, when prompted to identify the X-axis’s level of measurement and then asked to critique the chart again, Claude correctly recommended a bar chart because the X-axis used qualitative data._
### 7\. Provide Data and Request a Chart
This is the reverse of the tactic above. Provide the AI with a table and ask to plot it using several chart types. Requesting variants is an efficient way to ideate over charts (but use critical thinking, as mentioned above).
## Importing Tables into Design Tools
Now that you have sensible content, how do you get it into your design tool?
For charts, this is as easy as copying and pasting or importing the SVG file into the design tool. Tables are more challenging, however. Design tools have historically done a very poor job importing table data, but there are options.
For example, Figma has several community-made plugins that assist with importing data from spreadsheets. [_Google Sheets Sync_](https://www.figma.com/community/plugin/735770583268406934/google-sheets-sync) and [_Table Builder_](https://www.figma.com/community/plugin/1104128112873973808/table-builder?searchSessionId=ly7hf0o4-qjl1eil3rb8) are free plugins that import and synchronize spreadsheet data with Figma layers, helping you to populate a table efficiently.
_Figma has plugins like_ Table Builder _that enable you to copy and paste AI-generated data into your prototype._
However, there are issues with Figma’s third-party plugin model. These plugins can have usability issues and hidden costs, they may raise data-privacy concerns, or they may become abandoned and unsupported by their author.
More specialized and robust design tools, such as Axure, support importing spreadsheet files directly into prototype components. This feature can be a significant convenience for designers of data-intensive apps testing data-manipulation workflows.
_Axure allows importing data from a CSV-formatted file into a dedicated component that supports filtering, sorting, searching, pagination, and row manipulation as prototype interactions._
Regardless of your design tool, **do not import thousands of rows with these methods and do not attempt to create a complete simulation of a developed design** (you’ll probably break your design tool). Import just enough data to enhance the prototype’s content fidelity and support the tested interactions. A fully developed data table may contain thousands of records, but you may need to display only 50 realistic-looking rows in your prototype to support a testing task.
## Differences in AI Tools for Mock-Data Generation
AI tools have differences in their training and available tools; they do not handle tasks in the same way or with the same proficiency.
While exploring mock-data capabilities for this article, **Claude 3.5 Sonnet was easier to use and more reliably effective at generating tables and charts than ChatGPT 4o**.
|  |  **Claude 3.5 Sonnet** |  **ChatGPT 4o**  
---|---|---|---  
**Tables** |  Data Quality |  ✅ Generated data that more consistently followed requirements, such as enforcing unique values for a column, distributing values, or applying formatting |  ❌ Would claim that the generated data followed requirements when it did not, despite prompts to verify its output before finishing  
|  Numerical Accuracy |  ❌ Generated Python code but could not run it to confirm numerical accuracy |  ✅ Could run Python code to confirm numerical accuracy  
|  File Output |  ⚠️ Could not generate Excel or CSV files, but the data could be copied and pasted into a spreadsheet |  ✅ Generated Excel or CSV files containing the data for download  
**Charts** |  Generation |  ✅ Reliably created and modified charts when prompted (using the React-based Recharts library); applied best practices |  ⚠️ Reliably generated and modified various charts when prompted (using the Python-based matplotlib library); sometimes included unhelpful defaults (e.g., axes’ labels formatted in scientific notation, such as .2e6 for 200,000)  
|  Fonts |  ✅ Could use web-safe and system font families |  ❌ Had limited font family options and could not be prompted to use different ones  
|  Ease of Import into Design Tool |  ✅ Generated charts with text elements that were easy to copy, paste, and edit in a design tool (when prompted to use the SVG file format) |  ❌ Rendered chart text as vectors and not actual text elements, so the chart’s text could not be edited in the design tool  
Also, design tools such as Figma are experimenting with integrating AI-powered commands. These integrations are promising developments, as designers need more efficient workflows that prompt AI tools in their design context. But beware:
  * A general-purpose AI tool may be more effective at generating tables and charts than an AI feature embedded in Figma or another design tool.
  * It's unclear whether these AI-powered commands support revising a comprehensive dataset rather than independently filling separate elements with generated text or images.
  * Prompting from within the design tool may not retain the rich context and chat history available in a general-purpose AI tool such as Claude or ChatGPT. As a result, designers may find revising content more challenging.


AI tools are rapidly evolving, so today’s winner could be tomorrow’s loser as new model versions are released. But if you’re struggling to get desired results from your preferred AI tool, try a different tool instead (if you can). Its results may surprise you.
## Opportunities with Synthetic Data in Regulated Industries
This article has focused on filling tables with mock data, which is artificially generated and inspired by real data. However, it lacks high statistical fidelity and is used in small quantities. For many UX professionals, mock data is the pragmatic choice for their fast, iterative prototyping.
Yet, synthetic data may be helpful for UX professionals who work in highly regulated industries such as healthcare or finance. Synthetic data is derived from samples of actual data. Specialized AI tools use these samples to artificially generate new data that mimics various properties of the original, such as statistical patterns. Undesirable aspects (originating from those actual data samples) may also be adjusted, like personally identifiable information or human biases. The result is much more realistic data and in much larger quantities.
If a lack of representative data in your prototypes is a recurring problem, build relationships with others in your organization with similar needs. For example, with more authentic data, a presales team could customize more-understandable product demos for prospective customers, and a quality-assurance team could have more realistic testing builds to help them catch more functional defects before release. Forging alliances with other departments with similar pain points can justify the cost and effort of implementing a synthetic-data AI tool.
### Conclusion
Data-intensive applications are challenging to design, prototype, and present realistically. Despite the effort required, your prototype’s content fidelity must be high to gain the most valuable insights from usability testing. Clever use of generative AI can help create and refine the data necessary to make these experiences sensible to your meticulous users. Crafting realistic data is a chore, but now we have help.
### References
Laura Koesten, Kathleen Gregory, Paul Groth, and Elena Simperl. 2021. Talking datasets – understanding data sensemaking behaviours._International Journal of Human-Computer Studies_ 146, 102562. DOI:http://dx.doi.org/10.1016/j.ijhcs.2020.102562
## Related Courses
  * #### [UX Deliverables Effectively communicate ideas and findings to managers, collaborators, and other stakeholders  Interaction ](https://www.nngroup.com/courses/ux-deliverables/?lm=ai-data-prototype-testing&pt=article)
  * #### [Designing Complex Apps for Specialized Domains Create and evaluate applications for advanced decision making, complicated workflows, and complex domains  Interaction ](https://www.nngroup.com/courses/complex-apps-specialized-domains/?lm=ai-data-prototype-testing&pt=article)
  * #### [Content Strategy and Governance Techniques and tools for implementing an actionable content strategy  Management ](https://www.nngroup.com/courses/content-strategy/?lm=ai-data-prototype-testing&pt=article)


Artificial Intelligence,Prototyping,data,content,tables,complex applications
## Related Topics
  * Artificial Intelligence [Artificial Intelligence](https://www.nngroup.com/topic/ai/)
  * [Prototyping](https://www.nngroup.com/topic/prototyping/)


## Learn More:
  * [ Humanizing AI Does Not Help Your Users  Caleb Sponheim  · 4 min ](https://www.nngroup.com/videos/humanizing-ai-does-not-help/?lm=ai-data-prototype-testing&pt=article)
  * [ AI Strategy: 3 Key Questions  Caleb Sponheim  · 5 min ](https://www.nngroup.com/videos/ai-strategy-key-questions/?lm=ai-data-prototype-testing&pt=article)
  * [ AI-Assisted Prototyping: Promise and Pitfalls  Megan Brown  · 5 min ](https://www.nngroup.com/videos/ai-assisted-prototyping/?lm=ai-data-prototype-testing&pt=article)


## Related Articles:
  * [ Promptframes: Evolving the Wireframe for the Age of AI Evan Sunwall  · 12 min ](https://www.nngroup.com/articles/promptframes/?lm=ai-data-prototype-testing&pt=article)
  * [ Designing AI Products and Features: Study Guide Tanner Kohler  · 4 min ](https://www.nngroup.com/articles/designing-ai-study-guide/?lm=ai-data-prototype-testing&pt=article)
  * [ How AI Works and How Users Think About It: Study Guide Tanner Kohler  · 4 min ](https://www.nngroup.com/articles/ai-functionality-study-guide/?lm=ai-data-prototype-testing&pt=article)
  * [ When Should We Trust AI? Magic-8-Ball Thinking Caleb Sponheim  · 8 min ](https://www.nngroup.com/articles/ai-magic-8-ball/?lm=ai-data-prototype-testing&pt=article)
  * [ Prompt Controls in GenAI Chatbots: 4 Main Uses and Best Practices Feifei Liu  · 11 min ](https://www.nngroup.com/articles/prompt-controls-genai/?lm=ai-data-prototype-testing&pt=article)
  * [ Artificial Intelligence: Glossary Caleb Sponheim  · 5 min ](https://www.nngroup.com/articles/artificial-intelligence-glossary/?lm=ai-data-prototype-testing&pt=article)


## Subscribe to Our Newsletter
Get weekly UX articles, videos, and upcoming training events straight to your inbox.
Email
## Follow Us
  * [ LinkedIn ](https://www.linkedin.com/company/nielsen-norman-group)
  * [ Instagram ](https://www.instagram.com/nngux)
  * [ Youtube ](https://www.youtube.com/channel/UC2oCugzU6W8-h95W7eBTUEg)
  * [ Podcast ](https://podcasters.spotify.com/pod/show/nngroup )
  * [ X (Twitter) ](https://x.com/nngroup)
  * [ Facebook ](https://www.facebook.com/nngux)


  * Certification
    * [What is UX Certification?](https://www.nngroup.com/ux-certification/)
    * [Specialties](https://www.nngroup.com/ux-certification/specialties/)
    * [Exams](https://www.nngroup.com/ux-certification/exams/)
    * [UX Certified People](https://www.nngroup.com/ux-certification/people/)
  * UX Training
    * [All Live Courses](https://www.nngroup.com/courses/)
    * [Live Online Training Events](https://www.nngroup.com/training/live-courses/)
    * [Private Team Training](https://www.nngroup.com/team-training/)
    * [Course Calendar](https://www.nngroup.com/course-calendar/)
  * Consulting
    * [Expert Review](https://www.nngroup.com/consulting/expert-review/)
    * [User Testing](https://www.nngroup.com/consulting/user-testing/)
    * [Customized Research](https://www.nngroup.com/consulting/user-research/)
    * [Applied Workshops](https://www.nngroup.com/consulting/applied-workshops/)
    * [Keynote Speaking](https://www.nngroup.com/consulting/keynote-speaking/)
  * Free Guidance
    * [Articles & Videos](https://www.nngroup.com/articles/)
    * [The NN/g UX Podcast](https://podcasters.spotify.com/pod/show/nngroup)
  * About
    * [Why NN/g](https://www.nngroup.com/about/why-nng/)
    * [About Us](https://www.nngroup.com/about/)
    * [People](https://www.nngroup.com/people/)
    * [Clients](https://www.nngroup.com/about/about-client-list/)
    * [Contact](https://www.nngroup.com/about/contact/)
    * [Privacy Policy](https://www.nngroup.com/privacy-policy/)


[Copyright](https://www.nngroup.com/copyright-and-reprint-info/) (C) 1998-2025 Nielsen Norman Group, All Rights Reserved. 
  * Cookie Preferences
  * [Cookie Declaration](https://www.nngroup.com/cookie-declaration/)
  * [Privacy Policy](https://www.nngroup.com/privacy-policy/)


  
Top
