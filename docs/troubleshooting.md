# GitHub Pages workflow troubleshooting

## "Resource not accessible by integration" when configuring Pages

The `actions/configure-pages` step calls the Pages REST API to create or update
the site. If the workflow token cannot call that API, the step fails with errors
similar to:

```
Warning: Get Pages site failed. Error: Not Found - https://docs.github.com/rest/pages/pages#get-a-apiname-pages-site
Error: Create Pages site failed. Error: Resource not accessible by integration - https://docs.github.com/rest/pages/pages#create-a-apiname-pages-site
```

Common causes are:

- GitHub Pages is disabled by the repository or organization policy, so the
  `GITHUB_TOKEN` cannot create the site.
- The workflow is running with a token that lacks the `pages:write` permission
  (for example, a token from a forked pull request).

To fix the issue:

1. Ensure GitHub Pages is allowed for the repository in the repository settings
   or organization policies.
2. Run the deploy workflow from a branch with a `GITHUB_TOKEN` that has
   `pages:write` and `id-token:write` permissions (the workflow already requests
   these permissions).
3. Re-run the Pages deploy workflow after the permissions are corrected.

If Pages is intentionally disabled and you still want the pipeline to succeed,
remove or guard the Pages deployment workflow to avoid running it in that
context.
