# REST API Design Guidelines - Microsoft 365 Developer Blog

- URL: https://devblogs.microsoft.com/microsoft365dev/rest-api-design-guidelines/
- Retrieved: 2025-12-18T10:14:19.986123+00:00

[Skip to main content](javascript:void\(0\))
[ Microsoft ](https://www.microsoft.com)
Dev Blogs
[ Dev Blogs ](https://devblogs.microsoft.com)
Dev Blogs 
  * [ Home ](https://devblogs.microsoft.com)
  * Developer
    * [Microsoft for Developers](https://developer.microsoft.com/blog)
    * [Visual Studio](https://devblogs.microsoft.com/visualstudio/)
    * [Visual Studio Code](https://devblogs.microsoft.com/vscode-blog)
    * [Develop from the cloud](https://devblogs.microsoft.com/develop-from-the-cloud/)
    * [All things Azure](https://devblogs.microsoft.com/all-things-azure/)
    * [Xcode](https://devblogs.microsoft.com/xcode/)
    * [DevOps](https://devblogs.microsoft.com/devops/)
    * [Windows Developer](https://blogs.windows.com/windowsdeveloper/)
    * [ISE Developer](https://devblogs.microsoft.com/ise/)
    * [Azure SDK](https://devblogs.microsoft.com/azure-sdk/)
    * [Command Line](https://devblogs.microsoft.com/commandline/)
    * [Aspire](https://devblogs.microsoft.com/aspire/)
  * Technology
    * [DirectX](https://devblogs.microsoft.com/directx/)
    * [Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/)
  * Languages
    * [C++](https://devblogs.microsoft.com/cppblog/)
    * [C#](https://devblogs.microsoft.com/dotnet/category/csharp/)
    * [F#](https://devblogs.microsoft.com/dotnet/category/fsharp/)
    * [TypeScript](https://devblogs.microsoft.com/typescript/)
    * [PowerShell Team](https://devblogs.microsoft.com/powershell/)
    * [Python](https://devblogs.microsoft.com/python/)
    * [Java](https://devblogs.microsoft.com/java/)
    * [Java Blog in Chinese](https://devblogs.microsoft.com/java-ch/)
    * [Go](https://devblogs.microsoft.com/go/)
  * .NET
    * [All .NET posts](https://devblogs.microsoft.com/dotnet/ )
    * [.NET Aspire](https://devblogs.microsoft.com/dotnet/category/dotnet-aspire/)
    * [.NET MAUI](https://devblogs.microsoft.com/dotnet/category/maui/)
    * [AI](https://devblogs.microsoft.com/dotnet/category/ai/)
    * [ASP.NET Core](https://devblogs.microsoft.com/dotnet/category/aspnetcore/)
    * [Blazor](https://devblogs.microsoft.com/dotnet/category/blazor/)
    * [Entity Framework](https://devblogs.microsoft.com/dotnet/category/entity-framework/)
    * [NuGet](https://devblogs.microsoft.com/dotnet/category/nuget/)
    * [Servicing](https://devblogs.microsoft.com/dotnet/category/maintenance-and-updates/)
    * [.NET Blog in Chinese](https://devblogs.microsoft.com/dotnet-ch/)
  * Platform Development
    * [#ifdef Windows](https://devblogs.microsoft.com/ifdef-windows/)
    * [Microsoft Foundry](https://devblogs.microsoft.com/foundry/)
    * [Azure Government](https://devblogs.microsoft.com/azuregov/)
    * [Azure VM Runtime Team](https://devblogs.microsoft.com/azure-vm-runtime/)
    * [Bing Dev Center](https://blogs.bing.com/Developers-Blog/)
    * [Microsoft Edge Dev](http://blogs.windows.com/msedgedev/)
    * [Microsoft Azure](http://azure.microsoft.com/blog/)
    * [Microsoft 365 Developer](https://devblogs.microsoft.com/microsoft365dev/)
    * [Microsoft Entra Identity Developer](https://devblogs.microsoft.com/identity/)
    * [Old New Thing](https://devblogs.microsoft.com/oldnewthing/)
    * [Power Platform](https://devblogs.microsoft.com/powerplatform/)
  * Data Development
    * [ Azure Cosmos DB](https://devblogs.microsoft.com/cosmosdb/)
    * [Azure Data Studio](https://cloudblogs.microsoft.com/sqlserver/?product=azure-data-studio)
    * [Azure SQL](https://devblogs.microsoft.com/azure-sql/)
    * [OData](https://devblogs.microsoft.com/odata/)
    * [Revolutions R](http://blog.revolutionanalytics.com/)
    * [Unified Data Model (IDEAs)](https://devblogs.microsoft.com/udm/)
    * [Microsoft Entra PowerShell](https://devblogs.microsoft.com/entrapowershell/)
  * More


Search Search


  * No results


Cancel
  * [Dev Blogs](https://devblogs.microsoft.com/)
  * [Microsoft 365 Developer Blog](https://devblogs.microsoft.com/microsoft365dev/)
  * REST API Design Guidelines


July 19th, 2016
0 reactions
# REST API Design Guidelines
[Office Add-ins team](https://devblogs.microsoft.com/microsoft365dev/author/office_platform)
## 

[Show more](javascript:)
We are pleased to announce that Microsoft is publishing its "REST API Design Guidelines" to the API community: <http://www.GitHub.com/microsoft/api-guidelines/>. 
These guidelines represent a multi-year, cross-company, collaborative process aggregating the collective experience of hundreds of engineers designing, operating, and running global scale cloud services from across Microsoft; and listening to feedback on our APIs from customers and partners.  We have attempted to incorporate those learnings along with industry best practices in the API space to create guidelines that API teams across Microsoft use on a daily basis.
Our hope in publishing these guidelines to the greater API community is twofold:
  * First, that we will **further stimulate feedback on our APIs** and our approach to building them - only through such feedback can we build products that match the evolving needs of our customers.
  * Second, as we have benefitted from others in the API design community who have shared their guidelines, we want to contribute back. We believe that organizations of almost any size building APIs can benefit from having their own design guidelines.  Many companies and even organizations such as the [Whitehouse](https://github.com/WhiteHouse/api-standards) have already published their design guidelines and it's our hope that by contributing ours to the community conversation, **we can add to the body of community knowledge and reusable content** so that anyone can draw upon more collective knowledge when looking to set standards and guidelines within their organization.


 
We recognize that in API design, there are multiple correct ways to do things (ex: snake-case vs. train_case vs. UpperPascalCase vs. …) and we are sharing these design guidelines as what we have settled-upon after much debate among Microsoft colleagues.  We expect that these guidelines will evolve over time and that your feedback will play a part in that evolution. 
## Origins
Naturally, the Microsoft REST API Guidelines [document on GitHub](http://www.github.com/microsoft/api-guidelines/) went through a number of iterations before being what you can read today. 
The effort got started from hearing two key points of feedback from customers:
  * **It should be easier to get started with Microsoft APIs** - Developers wanted to be able to run the curl tool against an API endpoint and get a human-readable result in just a few minutes
  * **APIs for Microsoft cloud services should be consistent** - Developers didn't care that an API to work with an Azure virtual machine and an API to work with a user's Office 365 documents were developed by different parts of the company, they were both from Microsoft and developers expected consistency.


 
One of the goals of the effort was to **find the right balance of detail in the guidelines**.  We wanted a document that sufficiently codified best practices, but was also approachable for individual contributor engineers and technical product/program managers.  
## Relationship with OData
The OASIS Open [OData](http://www.odata.org/) standard provides a great level of detail for API developers seeking wire-level interoperability; and while Microsoft teams are encouraged to follow OData (and benefit from the [broad OData ecosystem](http://www.odata.org/ecosystem/)), there are some cases where it was more specificity than teams needed and some cases where additional information was needed.  For any areas of deviation, we have worked to feed information back to the OASIS OData Technical Committee and many aspects of the latest OData v4.0 and OData v4.01 incorporate learnings from evolution of the Microsoft REST API Guidelines. 
## Relationship with the Open API Initiative (OAI)
We are proud that Microsoft is a member of the [Open API Initiative (OAI)](https://openapis.org/), the evolution of Swagger.  As the scope of OAI/Swagger efforts have expanded from [a framework and tooling](http://swagger.io/) to also include a [specification](https://github.com/OAI/OpenAPI-Specification), we believe there are more opportunities ahead for Microsoft colleagues to engage with the OAI community to continue to evolve both.
## Getting Started
If you have read this far, THANK YOU. 
You can find the Microsoft REST API Guidelines on GitHub: <http://www.GitHub.com/microsoft/api-guidelines/>.  We welcome your feedback and encourage the filing of [Issues](https://github.com/microsoft/api-guidelines/issues) and [Pull Requests](https://github.com/microsoft/api-guidelines/pulls). 
If you want to try some of our APIs implemented using these guidelines, we suggest taking a look at the Microsoft Graph, our consolidated endpoint for cloud services across Microsoft.  A great place to start is: <https://developer.microsoft.com/graph>
We look forward to hearing from you--  
-- Gareth and Rob
_Gareth Jones (@garethj_msft)  
Principal API Architect   
Applications and Services division_
_Rob Dolin (@RobDolin)  
Senior Program Manager   
Cloud and Enterprise division_
[ 0](https://devblogs.microsoft.com/microsoft365dev/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Fmicrosoft365dev%2Frest-api-design-guidelines%2F "Sign in to react")
  *   *   *   *   *   * 

 0 
0 
  * [ Share on Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://devblogs.microsoft.com/microsoft365dev/rest-api-design-guidelines/ "Share on Facebook")
  * [ Share on X ](https://twitter.com/intent/tweet?url=https://devblogs.microsoft.com/microsoft365dev/rest-api-design-guidelines/&text=REST API Design Guidelines "Share on X")
  * [ Share on Linkedin ](https://www.linkedin.com/shareArticle?mini=true&url=https://devblogs.microsoft.com/microsoft365dev/rest-api-design-guidelines/ "Share on LinkedIn")


Category
[SharePoint Framework](https://devblogs.microsoft.com/microsoft365dev/category/sharepoint-framework/)
Share
  * (https://www.facebook.com/sharer/sharer.php?u=https://devblogs.microsoft.com/microsoft365dev/rest-api-design-guidelines/)
  * (https://twitter.com/intent/tweet?url=https://devblogs.microsoft.com/microsoft365dev/rest-api-design-guidelines/&text=REST API Design Guidelines)
  * (https://www.linkedin.com/shareArticle?mini=true&url=https://devblogs.microsoft.com/microsoft365dev/rest-api-design-guidelines/)


## Author
[Office Add-ins team](https://devblogs.microsoft.com/microsoft365dev/author/office_platform)
## 0 comments
Discussion is closed. 
[Code of Conduct](https://answers.microsoft.com/en-us/page/codeofconduct)


## Read next
July 29, 2016
### [Removing Code-Based Sandbox Solutions in SharePoint Online](https://devblogs.microsoft.com/microsoft365dev/removing-code-based-sandbox-solutions-in-sharepoint-online/)
SharePoint team
August 2, 2016
### [Microsoft Graph: Azure AD Privileged Identity Management Preview APIs available in Beta](https://devblogs.microsoft.com/microsoft365dev/microsoft-graph-azure-ad-privileged-identity-management-apis-beta/)
Microsoft Graph team
## Stay informed
Get notified when new posts are published.
Email *
Country/Region * Select...United StatesAfghanistanÅland IslandsAlbaniaAlgeriaAmerican SamoaAndorraAngolaAnguillaAntarcticaAntigua and BarbudaArgentinaArmeniaArubaAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBarbadosBelarusBelgiumBelizeBeninBermudaBhutanBoliviaBonaireBosnia and HerzegovinaBotswanaBouvet IslandBrazilBritish Indian Ocean TerritoryBritish Virgin IslandsBruneiBulgariaBurkina FasoBurundiCabo VerdeCambodiaCameroonCanadaCayman IslandsCentral African RepublicChadChileChinaChristmas IslandCocos (Keeling) IslandsColombiaComorosCongoCongo (DRC)Cook IslandsCosta RicaCôte dIvoireCroatiaCuraçaoCyprusCzechiaDenmarkDjiboutiDominicaDominican RepublicEcuadorEgyptEl SalvadorEquatorial GuineaEritreaEstoniaEswatiniEthiopiaFalkland IslandsFaroe IslandsFijiFinlandFranceFrench GuianaFrench PolynesiaFrench Southern TerritoriesGabonGambiaGeorgiaGermanyGhanaGibraltarGreeceGreenlandGrenadaGuadeloupeGuamGuatemalaGuernseyGuineaGuinea-BissauGuyanaHaitiHeard Island and McDonald IslandsHondurasHong Kong SARHungaryIcelandIndiaIndonesiaIraqIrelandIsle of ManIsraelItalyJamaicaJan MayenJapanJerseyJordanKazakhstanKenyaKiribatiKoreaKosovoKuwaitKyrgyzstanLaosLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgMacau SARMadagascarMalawiMalaysiaMaldivesMaliMaltaMarshall IslandsMartiniqueMauritaniaMauritiusMayotteMexicoMicronesiaMoldovaMonacoMongoliaMontenegroMontserratMoroccoMozambiqueMyanmarNamibiaNauruNepalNetherlandsNew CaledoniaNew ZealandNicaraguaNigerNigeriaNiueNorfolk IslandNorth MacedoniaNorthern Mariana IslandsNorwayOmanPakistanPalauPalestinian AuthorityPanamaPapua New GuineaParaguayPeruPhilippinesPitcairn IslandsPolandPortugalPuerto RicoQatarRéunionRomaniaRwandaSabaSaint BarthélemySaint Kitts and NevisSaint LuciaSaint MartinSaint Pierre and MiquelonSaint Vincent and the GrenadinesSamoaSan MarinoSão Tomé and PríncipeSaudi ArabiaSenegalSerbiaSeychellesSierra LeoneSingaporeSint EustatiusSint MaartenSlovakiaSloveniaSolomon IslandsSomaliaSouth AfricaSouth Georgia and South Sandwich IslandsSouth SudanSpainSri LankaSt HelenaAscensionTristan da CunhaSurinameSvalbardSwedenSwitzerlandTaiwanTajikistanTanzaniaThailandTimor-LesteTogoTokelauTongaTrinidad and TobagoTunisiaTurkeyTurkmenistanTurks and Caicos IslandsTuvaluU.S. Outlying IslandsU.S. Virgin IslandsUgandaUkraineUnited Arab EmiratesUnited KingdomUruguayUzbekistanVanuatuVatican CityVenezuelaVietnamWallis and FutunaYemenZambiaZimbabwe
I would like to receive the Microsoft 365 Developer Blog Newsletter. [Privacy Statement.](https://go.microsoft.com/fwlink/?LinkId=521839)
Subscribe
Follow this blog
(https://www.facebook.com/M365Dev/ "facebook")(https://twitter.com/Microsoft365Dev "twitter")(https://www.linkedin.com/showcase/microsoft365dev "linkedin")(https://www.youtube.com/microsoft365developer "youtube")(https://devblogs.microsoft.com/microsoft365dev/feed/ "RSS Feed")
Are you sure you wish to delete this comment?
OK Cancel
[Sign in](https://devblogs.microsoft.com/microsoft365dev/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Fmicrosoft365dev%2Frest-api-design-guidelines%2F)
Theme
# Insert/edit link
Close 
Enter the destination URL
URL
Link Text
Open link in a new tab
Or link to existing content
Search


_No search term specified. Showing recent items._ _Search or use up and down arrow keys to select an item._


Cancel
##### Code Block
×
Paste your code snippet
Ok Cancel
 
What's new
  * [Surface Pro](https://www.microsoft.com/surface/devices/surface-pro)
  * [Surface Laptop](https://www.microsoft.com/surface/devices/surface-laptop)
  * [Surface Laptop Studio 2](https://www.microsoft.com/en-us/d/Surface-Laptop-Studio-2/8rqr54krf1dz)
  * [Copilot for organizations](https://www.microsoft.com/en-us/microsoft-copilot/organizations?icid=DSM_Footer_CopilotOrganizations)
  * [Copilot for personal use](https://www.microsoft.com/en-us/microsoft-copilot/for-individuals?form=MY02PT&OCID=GE_web_Copilot_Free_868g3t5nj)
  * [AI in Windows](https://www.microsoft.com/en-us/windows/ai-features?icid=DSM_Footer_WhatsNew_AIinWindows)
  * [Explore Microsoft products](https://www.microsoft.com/en-us/microsoft-products-and-apps)
  * [Windows 11 apps](https://www.microsoft.com/en-us/windows/apps-for-windows?icid=DSM_Footer_WhatsNew_Windows11apps)


Microsoft Store
  * [Account profile](https://account.microsoft.com/)
  * [Download Center](https://www.microsoft.com/en-us/download)
  * [Microsoft Store support](https://go.microsoft.com/fwlink/?linkid=2139749)
  * [Returns](https://www.microsoft.com/en-us/store/b/returns)
  * [Order tracking](https://www.microsoft.com/en-us/store/b/order-tracking)
  * [Certified Refurbished](https://www.microsoft.com/en-us/store/b/certified-refurbished-products)
  * [Microsoft Store Promise](https://www.microsoft.com/en-us/store/b/why-microsoft-store?icid=footer_why-msft-store_7102020)
  * [Flexible Payments](https://www.microsoft.com/en-us/store/b/payment-financing-options?icid=footer_financing_vcc)


Education
  * [Microsoft in education](https://www.microsoft.com/en-us/education)
  * [Devices for education](https://www.microsoft.com/en-us/education/devices/overview)
  * [Microsoft Teams for Education](https://www.microsoft.com/en-us/education/products/teams)
  * [Microsoft 365 Education](https://www.microsoft.com/en-us/education/products/microsoft-365)
  * [How to buy for your school](https://www.microsoft.com/education/how-to-buy)
  * [Educator training and development](https://education.microsoft.com/)
  * [Deals for students and parents](https://www.microsoft.com/en-us/store/b/education)
  * [AI for education](https://www.microsoft.com/en-us/education/ai-in-education)


Business
  * [Microsoft Cloud](https://www.microsoft.com/en-us/microsoft-cloud)
  * [Microsoft Security](https://www.microsoft.com/en-us/security)
  * [Dynamics 365](https://www.microsoft.com/en-us/dynamics-365)
  * [Microsoft 365](https://www.microsoft.com/en-us/microsoft-365/business)
  * [Microsoft Power Platform](https://www.microsoft.com/en-us/power-platform)
  * [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)
  * [Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365-copilot?icid=DSM_Footer_Microsoft365Copilot)
  * [Small Business](https://www.microsoft.com/en-us/store/b/business?icid=CNavBusinessStore)


Developer & IT
  * [Azure](https://azure.microsoft.com/en-us/)
  * [Microsoft Developer](https://developer.microsoft.com/en-us/)
  * [Microsoft Learn](https://learn.microsoft.com/)
  * [Support for AI marketplace apps](https://www.microsoft.com/software-development-companies/offers-benefits/isv-success?icid=DSM_Footer_SupportAIMarketplace&ocid=cmm3atxvn98)
  * [Microsoft Tech Community](https://techcommunity.microsoft.com/)
  * [Microsoft Marketplace](https://marketplace.microsoft.com?icid=DSM_Footer_Marketplace&ocid=cmm3atxvn98)
  * [Marketplace Rewards](https://www.microsoft.com/software-development-companies/offers-benefits/marketplace-rewards?icid=DSM_Footer_MarketplaceRewards&ocid=cmm3atxvn98)
  * [Visual Studio](https://visualstudio.microsoft.com/)


Company
  * [Careers](https://careers.microsoft.com/)
  * [About Microsoft](https://www.microsoft.com/about)
  * [Company news](https://news.microsoft.com/source/?icid=DSM_Footer_Company_CompanyNews)
  * [Privacy at Microsoft](https://www.microsoft.com/en-us/privacy?icid=DSM_Footer_Company_Privacy)
  * [Investors](https://www.microsoft.com/investor/default.aspx)
  * [Diversity and inclusion](https://www.microsoft.com/en-us/diversity/default?icid=DSM_Footer_Company_Diversity)
  * [Accessibility](https://www.microsoft.com/en-us/accessibility)
  * [Sustainability](https://www.microsoft.com/en-us/sustainability/)


[ Your Privacy Choices Opt-Out Icon Your Privacy Choices ](https://aka.ms/yourcaliforniaprivacychoices) [ Consumer Health Privacy ](https://go.microsoft.com/fwlink/?linkid=2259814)
  * [Sitemap](https://www.microsoft.com/en-us/sitemap1.aspx)
  * [Contact Microsoft](https://support.microsoft.com/contactus)
  * [Privacy ](https://go.microsoft.com/fwlink/?LinkId=521839)
  * [Manage cookies]
  * [Terms of use](https://go.microsoft.com/fwlink/?LinkID=206977)
  * [Trademarks](https://go.microsoft.com/fwlink/?linkid=2196228)
  * [Safety & eco](https://go.microsoft.com/fwlink/?linkid=2196227)
  * [Recycling](https://www.microsoft.com/en-us/legal/compliance/recycling)
  * [About our ads](https://choice.microsoft.com)
  * (C) Microsoft 2025
