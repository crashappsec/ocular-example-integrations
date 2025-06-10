# Ocular Integrations starters

Starter code for writing your own Ocular integrations.

The repoistory has 3 example containers:

- **[Downloader](/downloader/)**: An example "downloader" image.
  This container will perform a "download" of a target to scan.

- **[Crawler](/crawler/)**: An example "crawler" image.
  This container will enumerate targets, and then trigger pipelines to run on those targets.
  It can be ran on a schedule or ad-hoc.

- **[Uploader](/uploader/)**: An example "uploader" image.
  This container will be fed the paths of files to upload via CLI arguments
  
For more information on how these resources are configured and used within Ocular,
see the [Ocular docs](https://github.com/crashappsec/ocular?tab=readme-ov-file#definitions)