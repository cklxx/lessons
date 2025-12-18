# Azure REST API Guidelines Update - Azure SDK Blog

- URL: https://devblogs.microsoft.com/azure-sdk/azure-rest-api-guidelines-update/
- Retrieved: 2025-12-18T10:14:14.621861+00:00

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
  * [Azure SDK Blog](https://devblogs.microsoft.com/azure-sdk/)
  * Azure REST API Guidelines Update


Mandatory MFA
Prepare now for the impact of multifactor authentication on Azure Identity libraries.
[ Learn more ](https://aka.ms/azsdk/identity/mfa)
October 5th, 2021
0 reactions
# Azure REST API Guidelines Update
[ Mark ](https://devblogs.microsoft.com/azure-sdk/author/markweitzel) , 
[ Mike ](https://devblogs.microsoft.com/azure-sdk/author/mikekistler)
## 

[Show more](javascript:)
## Updated Guidelines
The Azure API team has released a major update to the [Microsoft Azure REST API Guidelines](http://aka.ms/azapi/guidelines). The updated guidelines have been extended and clarified to drive greater consistency across the entire portfolio of Azure service APIs. This consistency benefits customers that access Azure services directly through the REST APIs. The consistency also benefits users of the Azure SDKs and Azure CLI. The SDKs and CLI are based on the REST APIs, and in some cases are generated from the API definition. The presentation has also been revised to use a consistent format with the [Azure SDK guidelines](http://aka.ms/azsdk/guide).
## Considerations for Service Design
There's also a new "[Considerations for Service Design](https://aka.ms/azapi/considerations)" document, intended for teams designing new services. The document describes the general approach to API design for cloud services. Much of the new document applies to cloud-based APIs. The specific protocol of the API doesn't matter, as the guidelines can be applied beyond HTTP-based REST APIs.
## Summary
The primary focus of the REST API guidelines is Azure services. However, the guidelines can also serve as a reference when designing any REST API, particularly for cloud-based applications and services. To learn about key elements of the Azure API guidelines, see [Designing & Versioning HTTP/REST APIs](https://www.youtube.com/watch?v=9Ng00IlBCtw).
Whether you're updating an existing API or creating a new one, the revised guidelines will help you:
  * Create a more durable API.
  * Accelerate your development.
  * Yield cleaner, more consistent SDKs.


For example, the guidelines help you understand when to use PATCH vs. POST. You'll also understand why the HTTP action verb selection is an important decision that impacts your service design. In short, you'll be creating a delightful developer experience. Review these documents as you build out your Azure service. If you have any questions, don't hesitate to reach out to the API Stewardship team. Check out the [Azure REST API Guidelines](http://aka.ms/azapi/guidelines) today.
 
[Azure SDK Releases](https://aka.ms/azsdk/releases)
 
 
## Azure SDK Blog Contributions
Thanks for reading this Azure SDK blog post. We hope you learned something new, and we welcome you to share the post. We’re open to Azure SDK blog contributions from our readers. To get started, contact us at [azsdkblog@microsoft.com](mailto:azsdkblog@microsoft.com) with your idea, and we'll set you up as a guest blogger.
  * Azure SDK Website: [aka.ms/azsdk](https://aka.ms/azsdk)
  * Azure SDK Intro (3-minute video): [aka.ms/azsdk/intro](https://aka.ms/azsdk/intro)
  * Azure SDK Intro Deck (PowerPoint deck): [aka.ms/azsdk/intro/deck](https://aka.ms/azsdk/intro/deck)
  * Azure SDK Releases: [aka.ms/azsdk/releases](https://aka.ms/azsdk/releases)
  * Azure SDK Blog: [aka.ms/azsdk/blog](https://aka.ms/azsdk/blog)
  * Azure SDK Twitter: [twitter.com/AzureSDK](https://twitter.com/AzureSDK)
  * Azure SDK Design Guidelines: [aka.ms/azsdk/guide](https://aka.ms/azsdk/guide)
  * Azure REST API Guidelines: [aka.ms/azapi/guidelines](https://aka.ms/azapi/guidelines)
  * Azure SDKs & Tools: [azure.microsoft.com/downloads](https://azure.microsoft.com/downloads)
  * Azure SDK Central Repository: [github.com/azure/azure-sdk](https://github.com/azure/azure-sdk#azure-sdk)
  * Azure SDK for .NET: [github.com/azure/azure-sdk-for-net](https://github.com/azure/azure-sdk-for-net)
  * Azure SDK for Java: [github.com/azure/azure-sdk-for-java](https://github.com/azure/azure-sdk-for-java)
  * Azure SDK for Python: [github.com/azure/azure-sdk-for-python](https://github.com/azure/azure-sdk-for-python)
  * Azure SDK for JavaScript/TypeScript: [github.com/azure/azure-sdk-for-js](https://github.com/azure/azure-sdk-for-js)
  * Azure SDK for Android: [github.com/Azure/azure-sdk-for-android](https://github.com/Azure/azure-sdk-for-android)
  * Azure SDK for iOS: [github.com/Azure/azure-sdk-for-ios](https://github.com/Azure/azure-sdk-for-ios)
  * Azure SDK for Go: [github.com/Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go)
  * Azure SDK for C: [github.com/Azure/azure-sdk-for-c](https://github.com/Azure/azure-sdk-for-c)
  * Azure SDK for C++: [github.com/Azure/azure-sdk-for-cpp](https://github.com/Azure/azure-sdk-for-cpp)


[ 0](https://devblogs.microsoft.com/azure-sdk/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Fazure-sdk%2Fazure-rest-api-guidelines-update%2F "Sign in to react")
  *   *   *   *   *   * 

 0 
0 
  * [ Share on Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://devblogs.microsoft.com/azure-sdk/azure-rest-api-guidelines-update/ "Share on Facebook")
  * [ Share on X ](https://twitter.com/intent/tweet?url=https://devblogs.microsoft.com/azure-sdk/azure-rest-api-guidelines-update/&text=Azure REST API Guidelines Update "Share on X")
  * [ Share on Linkedin ](https://www.linkedin.com/shareArticle?mini=true&url=https://devblogs.microsoft.com/azure-sdk/azure-rest-api-guidelines-update/ "Share on LinkedIn")


Category
[Azure SDK](https://devblogs.microsoft.com/azure-sdk/category/azure-sdk/)
Topics
[API](https://devblogs.microsoft.com/azure-sdk/tag/api/)[azure](https://devblogs.microsoft.com/azure-sdk/tag/azure/)[GUIDELINES](https://devblogs.microsoft.com/azure-sdk/tag/guidelines/)[REST](https://devblogs.microsoft.com/azure-sdk/tag/rest/)[REST APIs](https://devblogs.microsoft.com/azure-sdk/tag/rest-apis/)
Share
  * (https://www.facebook.com/sharer/sharer.php?u=https://devblogs.microsoft.com/azure-sdk/azure-rest-api-guidelines-update/)
  * (https://twitter.com/intent/tweet?url=https://devblogs.microsoft.com/azure-sdk/azure-rest-api-guidelines-update/&text=Azure REST API Guidelines Update)
  * (https://www.linkedin.com/shareArticle?mini=true&url=https://devblogs.microsoft.com/azure-sdk/azure-rest-api-guidelines-update/)


## Author
[Mark W.](https://devblogs.microsoft.com/azure-sdk/author/markweitzel)
Principal Architect
[Mike Kistler](https://devblogs.microsoft.com/azure-sdk/author/mikekistler)
Principal Program Manager
## 0 comments
Discussion is closed. 
[Code of Conduct](https://answers.microsoft.com/en-us/page/codeofconduct)


## Read next
October 7, 2021
### [Announcing the new Azure Monitor Query client libraries](https://devblogs.microsoft.com/azure-sdk/announcing-the-new-azure-monitor-query-client-libraries/)
Scott Addie
October 8, 2021
### [Introducing experimental OpenTelemetry support in the Azure SDK for .NET](https://devblogs.microsoft.com/azure-sdk/introducing-experimental-opentelemetry-support-in-the-azure-sdk-for-net/)
Pavel Krymets
## Stay informed
Get notified when new posts are published.
Email *
Country/Region * Select...United StatesAfghanistanÅland IslandsAlbaniaAlgeriaAmerican SamoaAndorraAngolaAnguillaAntarcticaAntigua and BarbudaArgentinaArmeniaArubaAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBarbadosBelarusBelgiumBelizeBeninBermudaBhutanBoliviaBonaireBosnia and HerzegovinaBotswanaBouvet IslandBrazilBritish Indian Ocean TerritoryBritish Virgin IslandsBruneiBulgariaBurkina FasoBurundiCabo VerdeCambodiaCameroonCanadaCayman IslandsCentral African RepublicChadChileChinaChristmas IslandCocos (Keeling) IslandsColombiaComorosCongoCongo (DRC)Cook IslandsCosta RicaCôte dIvoireCroatiaCuraçaoCyprusCzechiaDenmarkDjiboutiDominicaDominican RepublicEcuadorEgyptEl SalvadorEquatorial GuineaEritreaEstoniaEswatiniEthiopiaFalkland IslandsFaroe IslandsFijiFinlandFranceFrench GuianaFrench PolynesiaFrench Southern TerritoriesGabonGambiaGeorgiaGermanyGhanaGibraltarGreeceGreenlandGrenadaGuadeloupeGuamGuatemalaGuernseyGuineaGuinea-BissauGuyanaHaitiHeard Island and McDonald IslandsHondurasHong Kong SARHungaryIcelandIndiaIndonesiaIraqIrelandIsle of ManIsraelItalyJamaicaJan MayenJapanJerseyJordanKazakhstanKenyaKiribatiKoreaKosovoKuwaitKyrgyzstanLaosLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgMacau SARMadagascarMalawiMalaysiaMaldivesMaliMaltaMarshall IslandsMartiniqueMauritaniaMauritiusMayotteMexicoMicronesiaMoldovaMonacoMongoliaMontenegroMontserratMoroccoMozambiqueMyanmarNamibiaNauruNepalNetherlandsNew CaledoniaNew ZealandNicaraguaNigerNigeriaNiueNorfolk IslandNorth MacedoniaNorthern Mariana IslandsNorwayOmanPakistanPalauPalestinian AuthorityPanamaPapua New GuineaParaguayPeruPhilippinesPitcairn IslandsPolandPortugalPuerto RicoQatarRéunionRomaniaRwandaSabaSaint BarthélemySaint Kitts and NevisSaint LuciaSaint MartinSaint Pierre and MiquelonSaint Vincent and the GrenadinesSamoaSan MarinoSão Tomé and PríncipeSaudi ArabiaSenegalSerbiaSeychellesSierra LeoneSingaporeSint EustatiusSint MaartenSlovakiaSloveniaSolomon IslandsSomaliaSouth AfricaSouth Georgia and South Sandwich IslandsSouth SudanSpainSri LankaSt HelenaAscensionTristan da CunhaSurinameSvalbardSwedenSwitzerlandTaiwanTajikistanTanzaniaThailandTimor-LesteTogoTokelauTongaTrinidad and TobagoTunisiaTurkeyTurkmenistanTurks and Caicos IslandsTuvaluU.S. Outlying IslandsU.S. Virgin IslandsUgandaUkraineUnited Arab EmiratesUnited KingdomUruguayUzbekistanVanuatuVatican CityVenezuelaVietnamWallis and FutunaYemenZambiaZimbabwe
I would like to receive the Azure SDK Blog Newsletter. [Privacy Statement.](https://go.microsoft.com/fwlink/?LinkId=521839)
Subscribe
Follow this blog
(https://twitter.com/AzureSDK "twitter")(https://www.youtube.com/@AzureDevelopers "youtube")(https://github.com/Azure/azure-sdk "GitHub")(https://devblogs.microsoft.com/azure-sdk/feed/ "RSS Feed")
Are you sure you wish to delete this comment?
OK Cancel
[Sign in](https://devblogs.microsoft.com/azure-sdk/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Fazure-sdk%2Fazure-rest-api-guidelines-update%2F)
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
