-- python-resource-s3-library main module.
-- Renders async S3 client setup (aiobotocore) into the storage package.
--
-- The calling archetype is responsible for adding the corresponding
-- dependency to pyproject.toml:
--   aiobotocore[boto3]
--
-- API:
--   local s3 = require("python-resource-s3")
--   s3.render(context, { destination = context:get("project-name") })

local M = {}

function M.render(context, opts)
    opts = opts or {}
    local d = opts.destination
    if d and d ~= "" then
        directory.render("contents", context, { destination = d })
    else
        directory.render("contents", context)
    end
    return context
end

return M
