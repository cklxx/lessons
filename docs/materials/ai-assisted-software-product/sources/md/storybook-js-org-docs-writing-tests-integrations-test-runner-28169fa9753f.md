# Test runner | Storybook docs

- URL: https://storybook.js.org/docs/writing-tests/integrations/test-runner
- Retrieved: 2025-12-17T17:05:21.618776+00:00

[Storybook MCP sneak peek: Get early access](https://storybook.js.org/blog/storybook-mcp-sneak-peek/)
[](/)
  * [Docs](/docs)
  * [Addons](/addons)
  * [Showcase](/showcase)
  * [Blog](/blog)
  * [Visual Test](https://www.chromatic.com/storybook?utm_source=storybook_website&utm_medium=global_nav&utm_campaign=storybook)
  * [Enterprise](https://www.chromatic.com/enterprise?utm_source=storybook_website&utm_medium=global_nav&utm_campaign=storybook)


[88,807](https://github.com/storybookjs/storybook)
Search docs
[Get Started](/docs)
Docs 
Docs » Testing » Integrations » Test runner (Webpack)
[Documentation](/docs)[API](/docs/api)[Tutorials](/tutorials)[Addons](/integrations)[Changelog](/releases)
Version 10.1
  * [Get Started](/docs/get-started)
    * [Why Storybook?](/docs/get-started/why-storybook)
    * [Install](/docs/get-started/install)
    * Frameworks
    * [What's a story?](/docs/get-started/whats-a-story)
    * [Browse stories](/docs/get-started/browse-stories)
    * [Setup](/docs/get-started/setup)
    * [Conclusion](/docs/get-started/conclusion)
  * [Stories](/docs/writing-stories)
    * [Args](/docs/writing-stories/args)
    * [Parameters](/docs/writing-stories/parameters)
    * [Decorators](/docs/writing-stories/decorators)
    * [Play function](/docs/writing-stories/play-function)
    * [Loaders](/docs/writing-stories/loaders)
    * [Tags](/docs/writing-stories/tags)
    * [Naming components and hierarchy](/docs/writing-stories/naming-components-and-hierarchy)
    * Mocking data and modules
    * [Building pages and screens](/docs/writing-stories/build-pages-with-storybook)
    * [Stories for multiple components](/docs/writing-stories/stories-for-multiple-components)
    * [Writing stories in TypeScript](/docs/writing-stories/typescript)
  * [Testing](/docs/writing-tests)
    * [Interaction tests](/docs/writing-tests/interaction-testing)
    * [Accessibility tests](/docs/writing-tests/accessibility-testing)
    * [Visual tests](/docs/writing-tests/visual-testing)
    * [Snapshot tests](/docs/writing-tests/snapshot-testing)
    * [Test coverage](/docs/writing-tests/test-coverage)
    * [In CI](/docs/writing-tests/in-ci)
    * Integrations
  * [Docs](/docs/writing-docs)
    * [Autodocs](/docs/writing-docs/autodocs)
    * [MDX](/docs/writing-docs/mdx)
    * [Doc blocks](/docs/writing-docs/doc-blocks)
    * [Code panel](/docs/writing-docs/code-panel)
    * [Preview and build docs](/docs/writing-docs/build-documentation)
  * [Sharing](/docs/sharing)
    * [Publish](/docs/sharing/publish-storybook)
    * [Embed](/docs/sharing/embed)
    * [Design integrations](/docs/sharing/design-integrations)
    * [Composition](/docs/sharing/storybook-composition)
    * [Package Composition](/docs/sharing/package-composition)
  * [Essentials](/docs/essentials)
    * [Actions](/docs/essentials/actions)
    * [Backgrounds](/docs/essentials/backgrounds)
    * [Controls](/docs/essentials/controls)
    * [Highlight](/docs/essentials/highlight)
    * [Measure & outline](/docs/essentials/measure-and-outline)
    * [Toolbars & globals](/docs/essentials/toolbars-and-globals)
    * [Viewport](/docs/essentials/viewport)
  * [Addons](/docs/addons)
    * [Install](/docs/addons/install-addons)
    * [Write](/docs/addons/writing-addons)
    * [Configure addons](/docs/addons/configure-addons)
    * [Write a preset](/docs/addons/writing-presets)
    * [Add to catalog](/docs/addons/integration-catalog)
    * [Types of addons](/docs/addons/addon-types)
    * [Knowledge base](/docs/addons/addon-knowledge-base)
    * [Addon API](/docs/addons/addons-api)
    * [Migrate addons to 10.0](/docs/addons/addon-migration-guide)
  * [Configure](/docs/configure)
    * [Styling and CSS](/docs/configure/styling-and-css)
    * [Telemetry](/docs/configure/telemetry)
    * Integration
    * [Story rendering](/docs/configure/story-rendering)
    * [Story layout](/docs/configure/story-layout)
    * User Interface
    * [Environment variables](/docs/configure/environment-variables)
  * [Builders](/docs/builders)
    * [Vite](/docs/builders/vite)
    * [Webpack](/docs/builders/webpack)
    * [API](/docs/builders/builder-api)
  * [API](/docs/api)
    * main.js|ts configuration
    * [Component Story Format (CSF)](/docs/api/csf)
    * [ArgTypes](/docs/api/arg-types)
    * [Parameters](/docs/api/parameters)
    * Doc Blocks
    * Portable Stories
    * [Frameworks](/docs/api/new-frameworks)
    * [CLI options](/docs/api/cli-options)
  * [Releases](/docs/releases)
    * [Migrate to Storybook 10](/docs/releases/migration-guide)
    * [Migrate from 8 to 9](/docs/releases/migration-guide-from-older-version)
    * [Upgrading](/docs/releases/upgrading)
    * [Feature Lifecycle](/docs/releases/features)
    * [Roadmap](/docs/releases/roadmap)
  * [Contribute](/docs/contribute)
    * [RFC process](/docs/contribute/RFC)
    * [Code](/docs/contribute/code)
    * Documentation
    * [Frameworks](/docs/contribute/framework)
    * [Reproduce](/docs/contribute/how-to-reproduce)
  * [FAQ](/docs/faq)


# Test runner
ReactVueAngularWeb ComponentsMore
⚠️
The test runner has been superseded by the [Vitest addon](./vitest-addon), which offers the same functionality, powered by the faster and more modern [Vitest](https://vitest.dev/) browser mode. It also enables the full Storybook Test experience, allowing you to run interaction, accessibility, and visual tests from your Storybook app.
If you are using a Vite-powered Storybook framework, we recommend using the Vitest addon instead of the test runner.
Storybook test runner turns all of your stories into executable tests. It is powered by [Jest](https://jestjs.io/) and [Playwright](https://playwright.dev/).
  * For those [without a play function](../../writing-stories): it verifies whether the story renders without any errors.
  * For those [with a play function](../../writing-stories/play-function): it also checks for errors in the play function and that all assertions passed.


These tests run in a live browser and can be executed via the [command line](#cli-options) or your [CI server](#set-up-ci-to-run-tests).
## 
[Setup](#setup)
The test-runner is a standalone, framework-agnostic utility that runs parallel to your Storybook. You will need to take some additional steps to set it up properly. Detailed below is our recommendation to configure and execute it.
Run the following command to install it.
npm
    
    npm install @storybook/test-runner --save-dev
Update your `package.json` scripts and enable the test runner.
package.json
    
    {
      "scripts": {
        "test-storybook": "test-storybook"
      }
    }
Start your Storybook with:
npm
    
    npm run storybook
💡
Storybook's test runner requires either a locally running Storybook instance or a published Storybook to run all the existing tests.
Finally, open a new terminal window and run the test-runner with:
npm
    
    npm run test-storybook
## 
[Configure](#configure)
Test runner offers zero-config support for Storybook. However, you can run `test-storybook --eject` for more fine-grained control. It generates a `test-runner-jest.config.js` file at the root of your project, which you can modify. Additionally, you can extend the generated configuration file and provide [testEnvironmentOptions](https://github.com/playwright-community/jest-playwright#configuration) as the test runner also uses [jest-playwright](https://github.com/playwright-community/jest-playwright) under the hood.
### 
[CLI Options](#cli-options)
The test-runner is powered by [Jest](https://jestjs.io/) and accepts a subset of its [CLI options](https://jestjs.io/docs/cli) (for example, `--watch`, `--maxWorkers`). If you're already using any of those flags in your project, you should be able to migrate them into Storybook's test-runner without any issues. Listed below are all the available flags and examples of using them.
Options| Description  
---|---  
`--help`| Output usage information   
`test-storybook --help`  
`-s`, `--index-json`| Run in index json mode. Automatically detected (requires a compatible Storybook)   
`test-storybook --index-json`  
`--no-index-json`| Disables index json mode   
`test-storybook --no-index-json`  
`-c`, `--config-dir [dir-name]`| Directory where to load Storybook configurations from   
`test-storybook -c .storybook`  
`--watch`| Run in watch mode   
`test-storybook --watch`  
`--watchAll`| Watch files for changes and rerun all tests when something changes.  
`test-storybook --watchAll`  
`--coverage`| Runs [coverage tests](#generate-code-coverage) on your stories and components   
`test-storybook --coverage`  
`--coverageDirectory`| Directory where to write coverage report output   
`test-storybook --coverage --coverageDirectory coverage/ui/storybook`  
`--url`| Define the URL to run tests in. Useful for custom Storybook URLs   
`test-storybook --url http://the-storybook-url-here.com`  
`--browsers`| Define browsers to run tests in. One or multiple of: chromium, firefox, webkit   
`test-storybook --browsers firefox chromium`  
`--maxWorkers [amount]`| Specifies the maximum number of workers the worker-pool will spawn for running tests   
`test-storybook --maxWorkers=2`  
`--testTimeout [amount]`| Defines the maximum time in milliseconds that a test can run before it is automatically marked as failed. Useful for long-running tests   
`test-storybook --testTimeout=60000`  
`--no-cache`| Disable the cache   
`test-storybook --no-cache`  
`--clearCache`| Deletes the Jest cache directory and then exits without running tests   
`test-storybook --clearCache`  
`--verbose`| Display individual test results with the test suite hierarchy   
`test-storybook --verbose`  
`-u`, `--updateSnapshot`| Use this flag to re-record every snapshot that fails during this test run   
`test-storybook -u`  
`--eject`| Creates a local configuration file to override defaults of the test-runner   
`test-storybook --eject`  
`--json`| Prints the test results in JSON. This mode will send all other test output and user messages to stderr.   
`test-storybook --json`  
`--outputFile`| Write test results to a file when the --json option is also specified.   
`test-storybook --json --outputFile results.json`  
`--junit`| Indicates that test information should be reported in a junit file.   
`test-storybook --**junit**`  
`--ci`| Instead of the regular behavior of storing a new snapshot automatically, it will fail the test and require Jest to be run with `--updateSnapshot`.   
`test-storybook --ci`  
`--shard [index/count]`| Requires CI. Splits the test suite execution into multiple machines   
`test-storybook --shard=1/8`  
`--failOnConsole`| Makes tests fail on browser console errors  
`test-storybook --failOnConsole`  
`--includeTags`| Experimental feature   
Defines a subset of stories to be tested if they match the enabled [tags](#experimental-filter-tests).   
`test-storybook --includeTags="test-only, pages"`  
`--excludeTags`| Experimental feature   
Prevents stories from being tested if they match the provided [tags](#experimental-filter-tests).   
`test-storybook --excludeTags="no-tests, tokens"`  
`--skipTags`| Experimental feature   
Configures the test runner to skip running tests for stories that match the provided [tags](#experimental-filter-tests).   
`test-storybook --skipTags="skip-test, layout"`  
npm
    
    npm run test-storybook -- --watch
### 
[Run tests against a deployed Storybook](#run-tests-against-a-deployed-storybook)
By default, the test-runner assumes that you're running it against a locally served Storybook on port `6006`. If you want to define a target URL to run against deployed Storybooks, you can use the `--url` flag:
npm
    
    npm run test-storybook -- --url https://the-storybook-url-here.com
Alternatively, you can set the `TARGET_URL` environment variable and run the test-runner:
    
    TARGET_URL=https://the-storybook-url-here.com yarn test-storybook
## 
[Run accessibility tests](#run-accessibility-tests)
When you have the [Accessibility addon](https://storybook.js.org/addons/@storybook/addon-a11y) installed, you can run accessibility tests alongside your interaction tests, using the test-runner.
For more details, including configuration options, see the [Accessibility testing documentation](../accessibility-testing).
## 
[Run snapshot tests](#run-snapshot-tests)
[Snapshot testing](../snapshot-testing) is a helpful tool for verifying that edge cases like errors are handled correctly. It can also be used to verify that the rendered output of a component is consistent across different test runs.
### 
[Set up](#set-up)
To enable snapshot testing with the test-runner, you'll need to take additional steps to set it up properly.
Add a new [configuration file](#test-hook-api) inside your Storybook directory with the following inside:
.storybook/test-runner.ts
Typescript
    
    import type { TestRunnerConfig } from '@storybook/test-runner';
     
    const config: TestRunnerConfig = {
      async postVisit(page, context) {
        // the #storybook-root element wraps the story. In Storybook 6.x, the selector is #root
        const elementHandler = await page.$('#storybook-root');
        const innerHTML = await elementHandler.innerHTML();
        expect(innerHTML).toMatchSnapshot();
      },
    };
     
    export default config;
💡
The `postVisit` hook allows you to extend the test runner's default configuration. Read more about them [here](#test-hook-api).
When you execute the test-runner (for example, with `yarn test-storybook`), it will run through all of your stories and run the snapshot tests, generating a snapshot file for each story in your project located in the `__snapshots__` directory.
### 
[Configure](#configure-1)
Out of the box, the test-runner provides an inbuilt snapshot testing configuration covering most use cases. You can also fine-tune the configuration to fit your needs via `test-storybook --eject` or by creating a `test-runner-jest.config.js` file at the root of your project.
#### 
[Override the default snapshot directory](#override-the-default-snapshot-directory)
The test-runner uses a specific naming convention and path for the generated snapshot files by default. If you need to customize the snapshot directory, you can define a custom snapshot resolver to specify the directory where the snapshots are stored.
Create a `snapshot-resolver.js` file to implement a custom snapshot resolver:
./snapshot-resolver.js
    
    import path from 'path';
     
    export default {
      resolveSnapshotPath: (testPath) => {
        const fileName = path.basename(testPath);
        const fileNameWithoutExtension = fileName.replace(/\.[^/.]+$/, '');
        // Defines the file extension for the snapshot file
        const modifiedFileName = `${fileNameWithoutExtension}.snap`;
     
        // Configure Jest to generate snapshot files using the following convention (./src/test/__snapshots__/Button.stories.snap)
        return path.join('./src/test/__snapshots__', modifiedFileName);
      },
      resolveTestPath: (snapshotFilePath, snapshotExtension) =>
        path.basename(snapshotFilePath, snapshotExtension),
      testPathForConsistencyCheck: 'example',
    };
Update the `test-runner-jest.config.js` file and enable the `snapshotResolver` option to use the custom snapshot resolver:
./test-runner-jest.config.js
    
    import { getJestConfig } from '@storybook/test-runner';
     
    const defaultConfig = getJestConfig();
     
    const config = {
      // The default Jest configuration comes from @storybook/test-runner
      ...defaultConfig,
      snapshotResolver: './snapshot-resolver.js',
    };
     
    export default config;
When the test-runner is executed, it will cycle through all of your stories and run the snapshot tests, generating a snapshot file for each story in your project located in the custom directory you specified.
#### 
[Customize snapshot serialization](#customize-snapshot-serialization)
By default, the test-runner uses [`jest-serializer-html`](https://github.com/algolia/jest-serializer-html) to serialize HTML snapshots. This may cause issues if you use specific CSS-in-JS libraries like [Emotion](https://emotion.sh/docs/introduction), Angular's `ng` attributes, or similar libraries that generate hash-based identifiers for CSS classes. If you need to customize the serialization of your snapshots, you can define a custom snapshot serializer to specify how the snapshots are serialized.
Create a `snapshot-serializer.js` file to implement a custom snapshot serializer:
./snapshot-serializer.js
    
    // The jest-serializer-html package is available as a dependency of the test-runner
    const jestSerializerHtml = require('jest-serializer-html');
     
    const DYNAMIC_ID_PATTERN = /"react-aria-\d+(\.\d+)?"/g;
     
    module.exports = {
      /*
       * The test-runner calls the serialize function when the test reaches the expect(SomeHTMLElement).toMatchSnapshot().
       * It will replace all dynamic IDs with a static ID so that the snapshot is consistent.
       * For instance, from <label id="react-aria970235672-:rl:" for="react-aria970235672-:rk:">Favorite color</label> to <label id="react-mocked_id" for="react-mocked_id">Favorite color</label>
       */
      serialize(val) {
        const withFixedIds = val.replace(DYNAMIC_ID_PATTERN, 'mocked_id');
        return jestSerializerHtml.print(withFixedIds);
      },
      test(val) {
        return jestSerializerHtml.test(val);
      },
    };
Update the `test-runner-jest.config.js` file and enable the `snapshotSerializers` option to use the custom snapshot resolver:
./test-runner-jest.config.js
    
    import { getJestConfig } from '@storybook/test-runner';
     
    const defaultConfig = getJestConfig();
     
    const config = {
      ...defaultConfig,
      snapshotSerializers: [
        // Sets up the custom serializer to preprocess the HTML before it's passed onto the test-runner
        './snapshot-serializer.js',
        ...defaultConfig.snapshotSerializers,
      ],
    };
     
    export default config;
When the test-runner executes your tests, it will introspect the resulting HTML, replacing the dynamically generated attributes with the static ones provided by the regular expression in the custom serializer file before snapshotting the component. This ensures that the snapshots are consistent across different test runs.
## 
[Generate code coverage](#generate-code-coverage)
Storybook also provides a [coverage addon](https://storybook.js.org/addons/@storybook/addon-coverage). It is powered by [Istanbul](https://istanbul.js.org/), which allows out-of-the-box code instrumentation for the most commonly used frameworks and builders in the JavaScript ecosystem.
### 
[Set up](#set-up-1)
Engineered to work alongside modern testing tools (e.g., [Playwright](https://playwright.dev/)), the coverage addon automatically instruments your code and generates code coverage data. For an optimal experience, we recommend using the test-runner alongside the coverage addon to run your tests.
Run the following command to install the addon.
npm
    
    npx storybook@latest add @storybook/addon-coverage
ℹ️
The CLI's [`add`](../../api/cli-options#add) command automates the addon's installation and setup. To install it manually, see our [documentation](../../addons/install-addons#manual-installation) on how to install addons.
Start your Storybook with:
npm
    
    npm run storybook
Finally, open a new terminal window and run the test-runner with:
npm
    
    npm run test-storybook -- --coverage
### 
[Configure](#configure-2)
By default, the [`@storybook/addon-coverage`](https://storybook.js.org/addons/@storybook/addon-coverage) offers zero-config support for Storybook and instruments your code via [`istanbul-lib-instrument`](https://www.npmjs.com/package/istanbul-lib-instrument) for [Webpack](https://webpack.js.org/), or [`vite-plugin-istanbul`](https://github.com/iFaxity/vite-plugin-istanbul) for [Vite](https://vitejs.dev/). However, you can extend your Storybook configuration file (i.e., `.storybook/main.js|ts`) and provide additional options to the addon. Listed below are the available options divided by builder and examples of how to use them.
CSF 3CSF Next 🧪
.storybook/main.ts
Typescript
    
    // For Vite support add the following import
    // import type { AddonOptionsVite } from '@storybook/addon-coverage';
     
    import type { AddonOptionsWebpack } from '@storybook/addon-coverage';
     
    // Replace your-framework with the framework and builder you are using (e.g., react-webpack5, vue3-webpack5)
    import type { StorybookConfig } from '@storybook/your-framework';
     
    const coverageConfig: AddonOptionsWebpack = {
      istanbul: {
        include: ['**/stories/**'],
        exclude: ['**/exampleDirectory/**'],
      },
    };
     
    const config: StorybookConfig = {
      stories: [],
      addons: [
        // Other Storybook addons
        {
          name: '@storybook/addon-coverage',
          options: coverageConfig,
        },
      ],
    };
     
    export default config;
Vite optionsOptions| Description| Type  
---|---|---  
`checkProd`| Configures the plugin to skip instrumentation in production environments  
`options: { istanbul: { checkProd: true,}}`| `boolean`  
`cwd`| Configures the working directory for the coverage tests.  
Defaults to `process.cwd()`  
`options: { istanbul: { cwd: process.cwd(),}}`| `string`  
`cypress`| Replaces the `VITE_COVERAGE` environment variable with `CYPRESS_COVERAGE`.  
Requires Cypress's [code coverage](https://docs.cypress.io/guides/tooling/code-coverage)  
`options: { istanbul: { cypress: true,}}`| `boolean`  
`exclude`| Overrides the [default exclude list](https://github.com/storybookjs/addon-coverage/blob/main/src/constants.ts) with the provided list of files or directories to exclude from coverage  
`options: { istanbul: { exclude: ['**/stories/**'],}}`| `Array<String>` or `string`  
`extension`| Extends the [default extension list](https://github.com/storybookjs/addon-coverage/blob/main/src/constants.ts) with the provided list of file extensions to include in coverage  
`options: { istanbul: { extension: ['.js', '.cjs', '.mjs'],}}`| `Array<String>` or `string`  
`forceBuildInstrument`| Configures the plugin to add instrumentation in build mode   
`options: { istanbul: { forceBuildInstrument: true,}}`| `boolean`  
`include`| Select the files to collect coverage  
`options: { istanbul: { include: ['**/stories/**'],}}`| `Array<String>` or `string`  
`nycrcPath`| Defines the relative path for the existing nyc [configuration file](https://github.com/istanbuljs/nyc?tab=readme-ov-file#configuration-files)  
`options: { istanbul: { nycrcPath: '../nyc.config.js',}}`| `string`  
`requireEnv`| Overrides the `VITE_COVERAGE` environment variable's value by granting access to the `env` variables  
`options: { istanbul: { requireEnv: true,}}`| `boolean`  
Webpack 5 optionsOptions| Description| Type  
---|---|---  
`autoWrap`| Provides support for top-level return statements by wrapping the program code in a function  
`options: { istanbul: { autoWrap: true,}}`| `boolean`  
`compact`| Condenses the output of the instrumented code. Useful for debugging  
`options: { istanbul: { compact: false,}}`| `boolean`  
`coverageVariable`| Defines the global variable name that Istanbul will use to store coverage results  
`options: { istanbul: { coverageVariable: '__coverage__',}}`| `string`  
`cwd`| Configures the working directory for the coverage tests.  
Defaults to `process.cwd()`  
`options: { istanbul: { cwd: process.cwd(),}}`| `string`  
`debug`| Enables the debug mode for additional logging information during the instrumentation process  
`options: { istanbul: { debug: true,}}`| `boolean`  
`esModules`| Enables support for ES Module syntax  
`options: { istanbul: { esModules: true,}}`| `boolean`  
`exclude`| Overrides the [default exclude list](https://github.com/storybookjs/addon-coverage/blob/main/src/constants.ts) with the provided list of files or directories to exclude from coverage  
`options: { istanbul: { exclude: ['**/stories/**'],}}`| `Array<String>` or `string`  
`extension`| Extends the [default extension list](https://github.com/storybookjs/addon-coverage/blob/main/src/constants.ts) with the provided list of file extensions to include in coverage  
`options: { istanbul: { extension: ['.js', '.cjs', '.mjs'],}}`| `Array<String>` or `string`  
`include`| Select the files to collect coverage  
`options: { istanbul: { include: ['**/stories/**'],}}`| `Array<String>` or `string`  
`nycrcPath`| Defines the relative path for the existing nyc [configuration file](https://github.com/istanbuljs/nyc?tab=readme-ov-file#configuration-files)  
`options: { istanbul: { nycrcPath: '../nyc.config.js',}}`| `string`  
`preserveComments`| Includes comments in the instrumented code  
`options: { istanbul: { preserveComments: true,}}`| `boolean`  
`produceSourceMap`| Configures Instanbul to generate a source map for the instrumented code  
`options: { istanbul: { produceSourceMap: true,}}`| `boolean`  
`sourceMapUrlCallback`| Defines a callback function invoked with the filename and the source map URL when a source map is generated  
`options: { istanbul: { sourceMapUrlCallback: (filename, url) => {},}}`| `function`  
### 
[What about other coverage reporting tools?](#what-about-other-coverage-reporting-tools)
Out of the box, code coverage tests work seamlessly with Storybook's test-runner and the [`@storybook/addon-coverage`](https://storybook.js.org/addons/@storybook/addon-coverage). However, that doesn't mean you can't use additional reporting tools (e.g., [Codecov](https://about.codecov.io/)). For instance, if you're working with [LCOV](https://wiki.documentfoundation.org/Development/Lcov), you can use the generated output (in `coverage/storybook/coverage-storybook.json`) and create your own report with:
    
    npx nyc report --reporter=lcov -t coverage/storybook --report-dir coverage/storybook
## 
[Set up CI to run tests](#set-up-ci-to-run-tests)
You can also configure the test-runner to run tests on a CI environment. Documented below are some recipes to help you get started.
### 
[Run against deployed Storybooks via Github Actions deployment](#run-against-deployed-storybooks-via-github-actions-deployment)
If you're publishing your Storybook with services such as [Vercel](https://vercel.com/) or [Netlify](https://docs.netlify.com/site-deploys/notifications/#github-commit-statuses), they emit a `deployment_status` event in GitHub Actions. You can use it and set the `deployment_status.target_url` as the `TARGET_URL` environment variable. Here's how:
.github/workflows/storybook-tests.yml
    
    name: Storybook Tests
     
    on: deployment_status
     
    jobs:
      test:
        timeout-minutes: 60
        runs-on: ubuntu-latest
        if: github.event.deployment_status.state == 'success'
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-node@v4
            with:
              node-version-file: '.nvmrc'
          - name: Install dependencies
            run: yarn
          - name: Install Playwright
            run: npx playwright install --with-deps
          - name: Run Storybook tests
            run: yarn test-storybook
            env:
              TARGET_URL: '${{ github.event.deployment_status.target_url }}'
💡
The published Storybook must be publicly available for this example to work. We recommend running the test server using the recipe [below](#run-against-non-deployed-storybooks) if it requires authentication.
### 
[Run against non-deployed Storybooks](#run-against-non-deployed-storybooks)
You can use your CI provider (for example, [GitHub Actions](https://github.com/features/actions), [GitLab Pipelines](https://docs.gitlab.com/ee/ci/pipelines/), [CircleCI](https://circleci.com/)) to build and run the test runner against your built Storybook. Here's a recipe that relies on third-party libraries, that is to say, [concurrently](https://www.npmjs.com/package/concurrently), [http-server](https://www.npmjs.com/package/http-server), and [wait-on](https://www.npmjs.com/package/wait-on) to build Storybook and run tests with the test-runner.
.github/workflows/storybook-tests.yml
    
    name: 'Storybook Tests'
     
    on: push
     
    jobs:
      test:
        timeout-minutes: 60
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-node@v4
            with:
              node-version-file: '.nvmrc'
          - name: Install dependencies
            run: yarn
          - name: Install Playwright
            run: npx playwright install --with-deps
          - name: Build Storybook
            run: yarn build-storybook --quiet
          - name: Serve Storybook and run tests
            run: |
              npx concurrently -k -s first -n "SB,TEST" -c "magenta,blue" \
                "npx http-server storybook-static --port 6006 --silent" \
                "npx wait-on tcp:127.0.0.1:6006 && yarn test-storybook"
💡
By default, Storybook outputs the [build](../../sharing/publish-storybook#build-storybook-as-a-static-web-application) to the `storybook-static` directory. If you're using a different build directory, you'll need to adjust the recipe accordingly.
## 
[Advanced configuration](#advanced-configuration)
### 
[Test hook API](#test-hook-api)
The test-runner renders a story and executes its [play function](../../writing-stories/play-function) if one exists. However, certain behaviors are impossible to achieve via the play function, which executes in the browser. For example, if you want the test-runner to take visual snapshots for you, this is possible via Playwright/Jest but must be executed in Node.
The test-runner exports test hooks that can be overridden globally to enable use cases like visual or DOM snapshots. These hooks give you access to the test lifecycle _before_ and _after_ the story is rendered. Listed below are the available hooks and an overview of how to use them.
Hook| Description  
---|---  
`prepare`| Prepares the browser for tests  
`async prepare({ page, browserContext, testRunnerConfig }) {}`  
`setup`| Executes once before all the tests run  
`setup() {}`  
`preVisit`| Executes before a story is initially visited and rendered in the browser  
`async preVisit(page, context) {}`  
`postVisit`| Executes after the story is visited and fully rendered  
`async postVisit(page, context) {}`  
💡
These test hooks are experimental and may be subject to breaking changes. We encourage you to test as much as possible within the story's [play function](../../writing-stories/play-function).
To enable the hooks API, you'll need to add a new configuration file inside your Storybook directory and set them up as follows:
.storybook/test-runner.ts
Typescript
    
    import type { TestRunnerConfig } from '@storybook/test-runner';
     
    const config: TestRunnerConfig = {
      // Hook that is executed before the test runner starts running tests
      setup() {
        // Add your configuration here.
      },
      /* Hook to execute before a story is initially visited before being rendered in the browser.
       * The page argument is the Playwright's page object for the story.
       * The context argument is a Storybook object containing the story's id, title, and name.
       */
      async preVisit(page, context) {
        // Add your configuration here.
      },
      /* Hook to execute after a story is visited and fully rendered.
       * The page argument is the Playwright's page object for the story
       * The context argument is a Storybook object containing the story's id, title, and name.
       */
      async postVisit(page, context) {
        // Add your configuration here.
      },
    };
     
    export default config;
💡
Except for the `setup` function, all other functions run asynchronously. Both `preVisit` and `postVisit` functions include two additional arguments, a [Playwright page](https://playwright.dev/docs/pages) and a context object which contains the `id`, `title`, and the `name` of the story.
When the test-runner executes, your existing tests will go through the following lifecycle:
  * The `setup` function is executed before all the tests run.
  * The context object is generated containing the required information.
  * Playwright navigates to the story's page.
  * The `preVisit` function is executed.
  * The story is rendered, and any existing `play` functions are executed.
  * The `postVisit` function is executed.


### 
[(Experimental) Filter tests](#experimental-filter-tests)
When you run the test-runner on Storybook, it tests every story by default. However, if you want to filter the tests, you can use the `tags` configuration option. Storybook originally introduced this feature to generate [automatic documentation](../../writing-docs/autodocs) for stories. But it can be further extended to configure the test-runner to run tests according to the provided tags using a similar configuration option or via CLI flags (e.g., `--includeTags`, `--excludeTags`, `--skipTags`), only available with the latest stable release (`0.15` or higher). Listed below are the available options and an overview of how to use them.
Option| Description  
---|---  
`exclude`| Prevents stories if they match the provided tags from being tested.  
`include`| Defines a subset of stories only to be tested if they match the enabled tags.  
`skip`| Skips testing on stories if they match the provided tags.  
.storybook/test-runner.ts
Typescript
    
    import type { TestRunnerConfig } from '@storybook/test-runner';
     
    const config: TestRunnerConfig = {
      tags: {
        include: ['test-only', 'pages'],
        exclude: ['no-tests', 'tokens'],
        skip: ['skip-test', 'layout'],
      },
    };
     
    export default config;
ℹ️
Running tests with the CLI flags takes precedence over the options provided in the configuration file and will override the available options in the configuration file.
#### 
[Disabling tests](#disabling-tests)
If you want to prevent specific stories from being tested by the test-runner, you can configure your story with a custom tag, enable it to the test-runner configuration file or run the test-runner with the `--excludeTags` [CLI](#cli-options) flag and exclude them from testing. This is helpful when you want to exclude stories that are not yet ready for testing or are irrelevant to your tests. For example:
CSF 3CSF Next 🧪
MyComponent.stories.ts|tsx
Typescript
    
    // Replace your-framework with the name of your framework
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { MyComponent } from './MyComponent';
     
    const meta = {
      component: MyComponent,
      //👇 Provides the `no-tests` tag to all stories in this file
      tags: ['no-tests'],
    } satisfies Meta<typeof MyComponent>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const ExcludeStory: Story = {
      //👇 Adds the `no-tests` tag to this story to exclude it from the tests when enabled in the test-runner configuration
      tags: ['no-tests'],
    };
#### 
[Run tests for a subset of stories](#run-tests-for-a-subset-of-stories)
To allow the test-runner only to run tests on a specific story or subset of stories, you can configure the story with a custom tag, enable it in the test-runner configuration file or run the test-runner with the `--includeTags` [CLI](#cli-options) flag and include them in your tests. For example, if you wanted to run tests based on the `test-only` tag, you can adjust your configuration as follows:
CSF 3CSF Next 🧪
MyComponent.stories.ts|tsx
Typescript
    
    // Replace your-framework with the name of your framework
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { MyComponent } from './MyComponent';
     
    const meta = {
      component: MyComponent,
      //👇 Provides the `test-only` tag to all stories in this file
      tags: ['test-only'],
    } satisfies Meta<typeof MyComponent>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const IncludeStory: Story = {
      //👇 Adds the `test-only` tag to this story to be included in the tests when enabled in the test-runner configuration
      tags: ['test-only'],
    };
ℹ️
Applying tags for the component's stories should either be done at the component level (using `meta`) or at the story level. Importing tags across stories is not supported in Storybook and won't work as intended.
#### 
[Skip tests](#skip-tests)
If you want to skip running tests on a particular story or subset of stories, you can configure your story with a custom tag, enable it in the test-runner configuration file, or run the test-runner with the `--skipTags` [CLI](#cli-options) flag. Running tests with this option will cause the test-runner to ignore and flag them accordingly in the test results, indicating that the tests are temporarily disabled. For example:
CSF 3CSF Next 🧪
MyComponent.stories.ts|tsx
Typescript
    
    // Replace your-framework with the name of your framework
    import type { Meta, StoryObj } from '@storybook/your-framework';
     
    import { MyComponent } from './MyComponent';
     
    const meta = {
      component: MyComponent,
      //👇 Provides the `skip-test` tag to all stories in this file
      tags: ['skip-test'],
    } satisfies Meta<typeof MyComponent>;
     
    export default meta;
    type Story = StoryObj<typeof meta>;
     
    export const SkipStory: Story = {
      //👇 Adds the `skip-test` tag to this story to allow it to be skipped in the tests when enabled in the test-runner configuration
      tags: ['skip-test'],
    };
### 
[Authentication for deployed Storybooks](#authentication-for-deployed-storybooks)
If you use a secure hosting provider that requires authentication to host your Storybook, you may need to set HTTP headers. This is mainly because of how the test runner checks the status of the instance and the index of its stories through fetch requests and Playwright. To do this, you can modify the test-runner configuration file to include the `getHttpHeaders` function. This function takes the URL of the fetch calls and page visits as input and returns an object containing the headers that need to be set.
.storybook/test-runner.ts
Typescript
    
    import type { TestRunnerConfig } from '@storybook/test-runner';
     
    const config: TestRunnerConfig = {
      getHttpHeaders: async (url) => {
        const token = url.includes('prod') ? 'prod-token' : 'dev-token';
        return {
          Authorization: `Bearer ${token}`,
        };
      },
    };
     
    export default config;
### 
[Helpers](#helpers)
The test-runner exports a few helpers that can be used to make your tests more readable and maintainable by accessing Storybook's internals (e.g., `args`, `parameters`). Listed below are the available helpers and an overview of how to use them.
.storybook/test-runner.ts
Typescript
    
    import type { TestRunnerConfig } from '@storybook/test-runner';
    import { getStoryContext, waitForPageReady } from '@storybook/test-runner';
     
    const config: TestRunnerConfig = {
      // Hook that is executed before the test runner starts running tests
      setup() {
        // Add your configuration here.
      },
      /* Hook to execute before a story is initially visited before being rendered in the browser.
       * The page argument is the Playwright's page object for the story.
       * The context argument is a Storybook object containing the story's id, title, and name.
       */
      async preVisit(page, context) {
        // Add your configuration here.
      },
      /* Hook to execute after a story is visited and fully rendered.
       * The page argument is the Playwright's page object for the story
       * The context argument is a Storybook object containing the story's id, title, and name.
       */
      async postVisit(page, context) {
        // Get the entire context of a story, including parameters, args, argTypes, etc.
        const storyContext = await getStoryContext(page, context);
     
        // This utility function is designed for image snapshot testing. It will wait for the page to be fully loaded, including all the async items (e.g., images, fonts, etc.).
        await waitForPageReady(page);
     
        // Add your configuration here.
      },
    };
     
    export default config;
#### 
[Accessing story information with the test-runner](#accessing-story-information-with-the-test-runner)
If you need to access information about the story, such as its parameters, the test-runner includes a helper function named `getStoryContext` that you can use to retrieve it. You can then use it to customize your tests further as needed. For example, if you need to configure Playwright's page [viewport size](https://playwright.dev/docs/api/class-page#page-set-viewport-size) to use the viewport size defined in the story's parameters, you can do so as follows:
.storybook/test-runner.ts
Typescript
    
    import type { TestRunnerConfig } from '@storybook/test-runner';
    import { getStoryContext } from '@storybook/test-runner';
    import { MINIMAL_VIEWPORTS } from 'storybook/viewport';
     
    const DEFAULT_VIEWPORT_SIZE = { width: 1280, height: 720 };
     
    const config: TestRunnerConfig = {
      async preVisit(page, story) {
        // Accesses the story's parameters and retrieves the viewport used to render it
        const context = await getStoryContext(page, story);
        const viewportName = context.parameters?.viewport?.defaultViewport;
        const viewportParameter = MINIMAL_VIEWPORTS[viewportName];
     
        if (viewportParameter) {
          const viewportSize = Object.entries(viewportParameter.styles).reduce(
            (acc, [screen, size]) => ({
              ...acc,
              // Converts the viewport size from percentages to numbers
              [screen]: parseInt(size),
            }),
            {},
          );
          // Configures the Playwright page to use the viewport size
          page.setViewportSize(viewportSize);
        } else {
          page.setViewportSize(DEFAULT_VIEWPORT_SIZE);
        }
      },
    };
     
    export default config;
#### 
[Working with assets](#working-with-assets)
If you're running a specific set of tests (e.g., image snapshot testing), the test-runner provides a helper function named `waitForPageReady` that you can use to ensure the page is fully loaded and ready before running the test. For example:
.storybook/test-runner.ts
Typescript
    
    import type { TestRunnerConfig } from '@storybook/test-runner';
     
    import { waitForPageReady } from '@storybook/test-runner';
     
    import { toMatchImageSnapshot } from 'jest-image-snapshot';
     
    const customSnapshotsDir = `${process.cwd()}/__snapshots__`;
     
    const config: TestRunnerConfig = {
      setup() {
        expect.extend({ toMatchImageSnapshot });
      },
      async postVisit(page, context) {
        // Awaits for the page to be loaded and available including assets (e.g., fonts)
        await waitForPageReady(page);
     
        // Generates a snapshot file based on the story identifier
        const image = await page.screenshot();
        expect(image).toMatchImageSnapshot({
          customSnapshotsDir,
          customSnapshotIdentifier: context.id,
        });
      },
    };
     
    export default config;
### 
[Index.json mode](#indexjson-mode)
The test-runner transforms your story files into tests when testing a local Storybook. For a remote Storybook, it uses the Storybook's [index.json](../../configure/index#feature-flags) (formerly `stories.json`) file (a static index of all the stories) to run the tests.
#### 
[Why?](#why)
Suppose you run into a situation where the local and remote Storybooks appear out of sync, or you might not even have access to the code. In that case, the `index.json` file is guaranteed to be the most accurate representation of the deployed Storybook you are testing. To test a local Storybook using this feature, use the `--index-json` flag as follows:
npm
    
    npm run test-storybook -- --index-json
💡
The `index.json` mode is not compatible with the watch mode.
If you need to disable it, use the `--no-index-json` flag:
npm
    
    npm run test-storybook -- --no-index-json
#### 
[How do I check if my Storybook has a `index.json` file?](#how-do-i-check-if-my-storybook-has-a-indexjson-file)
Index.json mode requires a `index.json` file. Open a browser window and navigate to your deployed Storybook instance (for example, `https://your-storybook-url-here.com/index.json`). You should see a JSON file that starts with a `"v": 3` key, immediately followed by another key called "stories", which contains a map of story IDs to JSON objects. If that is the case, your Storybook supports [index.json mode](../../configure/index#feature-flags).
## 
[What's the difference between Chromatic and Test runner?](#whats-the-difference-between-chromatic-and-test-runner)
The test-runner is a generic testing tool that can run locally or on CI and be configured or extended to run all kinds of tests.
[Chromatic](https://www.chromatic.com/?utm_source=storybook_website&utm_medium=link&utm_campaign=storybook) is a cloud-based service that runs [visual](../visual-testing) and [interaction tests](../interaction-testing) (and soon [accessibility tests](../accessibility-testing)) without setting up the test runner. It also syncs with your git provider and manages access control for private projects.
However, you might want to pair the test runner and Chromatic in some cases.
  * Use it locally and Chromatic on your CI.
  * Use Chromatic for visual and component tests and run other custom tests using the test runner.


## 
[Troubleshooting](#troubleshooting)
### 
[The test runner seems flaky and keeps timing out](#the-test-runner-seems-flaky-and-keeps-timing-out)
If your tests time out with the following message:
    
    Timeout - Async callback was not invoked within the 15000 ms timeout specified by jest.setTimeout
It might be that Playwright couldn't handle testing the number of stories you have in your project. Perhaps you have a large number of stories, or your CI environment has a really low RAM configuration. In such cases, you should limit the number of workers that run in parallel by adjusting your command as follows:
package.json
    
    {
      "scripts": {
        "test-storybook:ci": "yarn test-storybook --maxWorkers=2"
      }
    }
### 
[The error output in the CLI is too short](#the-error-output-in-the-cli-is-too-short)
By default, the test runner truncates error outputs at 1000 characters, and you can check the full output directly in Storybook in the browser. However, if you want to change that limit, you can do so by setting the `DEBUG_PRINT_LIMIT` environment variable to a number of your choosing, for example, `DEBUG_PRINT_LIMIT=5000 yarn test-storybook`.
### 
[Run the test runner in other CI environments](#run-the-test-runner-in-other-ci-environments)
As the test runner is based on Playwright, you might need to use specific docker images or other configurations depending on your CI setup. In that case, you can refer to the [Playwright CI docs](https://playwright.dev/docs/ci) for more information.
### 
[Tests filtered by tags are incorrectly executed](#tests-filtered-by-tags-are-incorrectly-executed)
If you've enabled filtering tests with tags and provided similar tags to the `include` and `exclude` lists, the test-runner will execute the tests based on the `exclude` list and ignore the `include` list. To avoid this, make sure the tags provided to the `include` and `exclude` lists differ.
### 
[The test runner doesn't support Yarn PnP out of the box](#the-test-runner-doesnt-support-yarn-pnp-out-of-the-box)
If you've enabled the test-runner in a project running on a newer version of Yarn with Plug'n'Play (PnP) enabled, the test-runner might not work as expected and may generate the following error when running tests:
    
    PlaywrightError: jest-playwright-preset: Cannot find playwright package to use chromium
This is due to the test-runner using the community-maintained package [jest-playwright-preset](https://github.com/playwright-community/jest-playwright) that still needs to support this feature. To solve this, you can either switch the [`nodeLinker`](https://yarnpkg.com/features/linkers) setting to `node-modules` or install Playwright as a direct dependency in your project, followed by adding the browser binaries via the [`install`](https://playwright.dev/docs/browsers#install-browsers) command.
### 
[Run test coverage in other frameworks](#run-test-coverage-in-other-frameworks)
If you intend on running coverage tests in frameworks with special files like Vue 3 or Svelte, you'll need to adjust your configuration and enable the required file extensions. For example, if you're using Vue, you'll need to add the following to your nyc configuration file (i.e., `.nycrc.json` or `nyc.config.js`):
JavaScript configurationJSON configuration
.nyc.config.js
    
    export default {
      // Other configuration options
      extension: ['.js', '.cjs', '.mjs', '.ts', '.tsx', '.jsx', '.vue'],
    };
### 
[The coverage addon doesn't support optimized builds](#the-coverage-addon-doesnt-support-optimized-builds)
If you generated a production build optimized for performance with the [`--test`](../../sharing/publish-storybook#customizing-the-build-for-performance) flag, and you're using the coverage addon to run tests against your Storybook, you may run into a situation where the coverage addon doesn't instrument your code. This is due to how the flag works, as it removes addons that have an impact on performance (e.g., [`Docs`](../../writing-docs), [coverage addon](https://storybook.js.org/addons/@storybook/addon-coverage)). To resolve this issue, you'll need to adjust your Storybook configuration file (i.e., `.storybook/main.js|ts`) and include the [`disabledAddons`](../../api/main-config/main-config-build#testdisabledaddons) option to allow the addon to run tests at the expense of a slower build.
CSF 3CSF Next 🧪
.storybook/main.ts
Typescript
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { StorybookConfig } from '@storybook/your-framework';
     
    const config: StorybookConfig = {
      framework: '@storybook/your-framework',
      stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
      addons: ['@storybook/addon-docs', '@storybook/addon-vitest', '@storybook/addon-coverage'],
      build: {
        test: {
          disabledAddons: ['@storybook/addon-docs'],
        },
      },
    };
     
    export default config;
### 
[The coverage addon doesn't support instrumented code](#the-coverage-addon-doesnt-support-instrumented-code)
As the [coverage addon](https://storybook.js.org/addons/@storybook/addon-coverage) is based on Webpack5 loaders and Vite plugins for code instrumentation, frameworks that don't rely upon these libraries (e.g., Angular configured with Webpack), will require additional configuration to enable code instrumentation. In that case, you can refer to the following [repository](https://github.com/yannbf/storybook-coverage-recipes) for more information.
**More testing resources**
  * [Interaction testing](../interaction-testing) for user behavior simulation
  * [Accessibility testing](../accessibility-testing) for accessibility
  * [Visual testing](../visual-testing) for appearance
  * [Snapshot testing](../snapshot-testing) for rendering errors and warnings
  * [Test coverage](../test-coverage) for measuring code coverage
  * [CI](../in-ci) for running tests in your CI/CD pipeline
  * [Vitest addon](./vitest-addon) for running tests in Storybook
  * [End-to-end testing](./stories-in-end-to-end-tests) for simulating real user scenarios
  * [Unit testing](./stories-in-unit-tests) for functionality


Was this page useful?
👍👎
[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/writing-tests/integrations/test-runner.mdx)
On this page


Join the community
Subscribe
7,044 developers and counting
[](http://github.com/storybookjs)[](https://bsky.app/profile/storybook.js.org)[](https://twitter.com/storybookjs)[](https://discord.gg/storybook)[](https://www.youtube.com/channel/UCr7Quur3eIyA_oe8FNYexfg)
Why
[Why Storybook](/docs/get-started/why-storybook)[Component driven UI](https://componentdriven.org/)
Docs
[Guides](/docs)[Tutorials](/tutorials)[Changelog](/releases)[Telemetry](/docs/configure/telemetry)
Community
[Addons](/integrations)[Get involved](/community)[Blog](/blog)
Showcase
[Explore](/showcase)[About](/showcase/about)
Open source software
Maintained by
[Chromatic](https://www.chromatic.com/storybook?utm_source=storybook_website&utm_medium=footer&utm_campaign=storybook)
Special thanks to [Netlify](https://netlify.com).
