## Project Altis Status

A lambda script to constantly update the Cachet status page at [status.projectalt.is](https://status.projectalt.is).

#### Env Vars


|   **variable**  | **Description**                       |
|:---------------:|---------------------------------------|
| username        | The username used to check login api. |
| password        | The password used to check login api. |
| login_metric_id | The login metric id                   |
| website_comp_id | The component ID for website          |
| login_comp_id   | The component ID for login            |
| mongo_comp_id   | The component ID for mongo            |
| mongo_url       | The URL to ping for mongo middleware  |
| mongo_username  | the http auth username                |
| mongo_password  | the http auth password                |
| cachet_token    | Cachet token to report statistics     |
| raven_dsn       | Raven DNS for tracking|

#### Lambda setup

zip the *contents* of the git repo, including the external modules, and upload to a lambda function.

Runtime: Python 3.6

Handler: lambda_function.lambda_handler

Role permissions: basic edge Lambda permissions

Timeout: at least 20 seconds

Resources needed: 128 MB (max memory used 30MB)

Triggers: Cloudwatch Events Scheduled expression: `cron(* /5 * * * ? *)`

#### License

MIT licensed. For more information see [LICENSE.md](LICENSE.md).