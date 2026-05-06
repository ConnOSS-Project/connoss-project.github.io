# Home

## ConnOSS (Connected Open Source Software)

ConnOSS is a DFG-funded research project that aims to help researchers showcase their software work and makes it easier for others to find and use research software. We believe that good research software should be visible, properly described, and easy to discover.

ConnOSS offers an automated infrastructure that generates consistent, harmonized, and enriched metadata for research software. Unlike manual metadata creation, which is time-consuming, or existing tools with limited coverage, ConnOSS streamlines the process—enabling researchers to enhance the visibility and FAIRness of their software with minimal effort.

ConnOSS is funded by the Deutsche Forschungsgemeinschaft (DFG) under grant number 561044496, as part of the "Research Data and Software" program within the [Scientific Library Services and Information Systems (LIS)](https://www.dfg.de/de/foerderung/foerdermoeglichkeiten/programme/infrastruktur/lis) funding scheme.

<div style="text-align: center; margin: 20px 0;">
  <img src="../images/DFG.png" alt="DFG Logo" style="height: 60px; margin: 10px;">
</div>

More information can be found at [DFG's GEPRIS research information system](https://gepris.dfg.de/gepris/projekt/561044496).

<p><a href="connoss_metadata.json" download style="font-weight: bold;"> 💾 Download JSON-LD metadata for ConnOSS project </a></p>

<p><a href="ro-crate-metadata.json" download style="font-weight: bold;"> 💼 Download RO-Crate for ConnOSS project </a></p>

<div style="text-align: center; margin: 40px 0;">
  <a href="about/" class="md-button md-button--primary" style="margin: 10px;">Learn More</a>
  <a href="team/" class="md-button md-button--primary" style="margin: 10px;">Meet the Team</a>
  <a href="blog/" class="md-button md-button--primary" style="margin: 10px;">Follow Our Progress</a>
</div>

<script type="application/json">
{
  "@context": "http://schema.org/",
  "@id": "https://w3id.org/connoss/",
  "@type": "ResearchProject",
  "name": "ConnOSS", 
  "foundingDate": "2025-09-01",
  "description": "ConnOSS is a DFG-funded research project that aims to help researchers showcase their software work and makes it easier for others to find and use research software. We believe that good research software should be visible, properly described, and easy to discover. ConnOSS offers an automated infrastructure that generates consistent, harmonized, and enriched metadata for research software. Unlike manual metadata creation, which is time-consuming, or existing tools with limited coverage, ConnOSS streamlines the process—enabling researchers to enhance the visibility and FAIRness of their software with minimal effort.",
  "keywords": "ConnOSS, research project, research software, software visibility, software discoverability, harmonized metadata, enriched metadata, FAIRness",
  "url": "https://connoss-project.github.io/",
  "logo": "https://connoss-project.github.io/images/logo.png", 
  "member": [
    {
      "@type": "Organization",
      "@id":"https://ror.org/0259fwx54",
      "name": "ZB MED – Information Centre for Life Sciences",
      "url": "https://www.zbmed.de/"
    },
    {
      "@type": "Organization",
      "@id":"https://ror.org/018afyw53",
      "name": "GESIS – Leibniz Institute for the Social Sciences",
      "url": "https://www.gesis.org/"
    },
    {
      "@type": "Organization",
      "@id":"https://ror.org/003sav189",
      "name": "OFFIS – Institute for Information Technology",
      "url": "https://www.offis.de/"
    },
    {
      "@type": "Organization",
      "@id":"https://ror.org/033n9gh91",
      "name": "Carl von Ossietzky Universität",
      "url": "https://uni-oldenburg.de/"
    },
    {
      "@type": "Person",
      "@id": "https://orcid.org/0000-0003-3986-0510",
      "givenName": "Leyla Jael",
      "familyName": "Castro",
      "affiliation": { "@id":"https://ror.org/0259fwx54" }
    },
    {
      "@type": "Person",
      "@id": "https://orcid.org/0000-0003-1793-9615",
      "givenName": "Brigitte",
      "familyName": "Mathiak",
      "affiiation": { "@id":"https://ror.org/018afyw53" }
    },
    {
      "@type": "Person",
      "@id": "https://orcid.org/0000-0003-1881-9172",
      "givenName": "Astrid",
      "familyName": "Nieße",
      "affiiation": { "@id":"https://ror.org/033n9gh91" }
    },
    {
      "@type": "Person",
      "@id": "https://orcid.org/0000-0001-9523-7227",
      "givenName": "Stephan",
      "familyName": "Ferenz",
      "affiliation": { "@id":"https://ror.org/003sav189" }
    },
    {
      "@type": "Person",
      "@id": "https://orcid.org/0000-0001-5844-3021",
      "givenName": "Lu",
      "familyName": "Gan",
      "affiiation": { "@id":"https://ror.org/018afyw53" }
    },
    {
      "@type": "Person",
      "@id": "https://orcid.org/0000-0002-6767-5905",
      "givenName": "Oliver",
      "familyName": "Werth",
      "affiliation": { "@id":"https://ror.org/003sav189" }
    },
    {
      "@type": "Person",
      "@id": "https://orcid.org/0000-0002-1435-0584",
      "givenName": "Aida",
      "familyName": "Jafarbigloo",
      "affiiation": { "@id":"https://ror.org/033n9gh91" }
    },
{
      "@type": "Person",
      "@id": "https://orcid.org/0009-0005-7305-3052",
      "givenName": "Suhasini",
      "familyName": "Venkatesh",
      "affiliation": { "@id":"https://ror.org/0259fwx54" }
    },
    {
      "@type": "Person",
      "@id": "https://orcid.org/0009-0008-7998-3965",
      "givenName": "Maryam",
      "familyName": "Sefidbari",
      "affiliation": { "@id":"https://ror.org/0259fwx54" }
    },
    {
      "@type": "Person",
      "@id": "https://orcid.org/0009-0003-9975-1321",
      "givenName": "Akhilan",
      "familyName": "Ashokan",
      "affiliation": { "@id":"https://ror.org/0259fwx54" }
    }
  ],  
  "funding": [
    {
      "@type": "Grant",
      "@id": "https://gepris.dfg.de/gepris/projekt/561044496",
      "funder": {
        "@type": "Organization",
        "@id": "https://ror.org/018mejw64",
        "name": "Deutsche Forschungsgemeinschaft", 
        "alternateName": "German Research Foundation",
        "url": "http://www.dfg.de/en/"  
      },
      "identifier": "561044496",
      "description": "Project no. 561044496, as part of the \"Research Data and Software\" program within the Scientific Library Services and Information Systems (LIS) funding scheme."
    }
  ],
"knowsAbout": [
    {
      "@type": "Report",
      "@id": "https://doi.org/10.5281/zenodo.15616384",
      "name": "Connected Open Source Software - ConnOSS - Proposal (Version v1.0.0)",
      "author": [
        { "@type": "Person", "@id": "https://orcid.org/0000-0003-3986-0510", "name": "Castro, L. J." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0003-1793-9615", "name": "Mathiak, B." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0003-1881-9172", "name": "Nieße, A." }
      ],
      "datePublished": "2025-06-07"
    },
    {
      "@type": "Poster",
      "@id": "https://doi.org/10.5281/zenodo.18835973",
      "name": "ConnOSS and Metadata Extraction for Research Software",
      "author": [
        { "@type": "Person", "@id": "https://orcid.org/0000-0002-1435-0584", "name": "Jafarbigloo, A." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0003-1793-9615", "name": "Mathiak, B." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0003-3986-0510", "name": "Castro, L. J." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0001-5844-3021", "name": "Gan, L." },
        { "@type": "Person", "@id": "https://orcid.org/0009-0008-7998-3965", "name": "Sefidbari, M." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0002-6767-5905", "name": "Werth, O." },
        { "@type": "Person", "@id": "https://orcid.org/0009-0005-7305-3052", "name": "Venkatesh, S." }
      ],
      "datePublished": "2026-03-02"
    },
    {
      "@type": "PresentationDigitalDocument",
      "name": "A metadata extraction tool for GitLab repositories",
      "@id": "https://doi.org/10.5281/zenodo.18837374",
      "author": [
        { "@type": "Person", "@id": "https://orcid.org/0009-0003-9975-1321", "name": "Ashokan, A." },
        { "@type": "Person", "@id": "https://orcid.org/0009-0005-7305-3052", "name": "Venkatesh, S." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0003-3986-0510", "name": "Castro, L. J." }
      ],
      "datePublished": "2026-03-02"
    },
    {
      "@type": "PresentationDigitalDocument",
      "name": "Initiatives at ZB MED and NFDI on metadata for software and AI models",
      "@id": "https://doi.org/10.5281/zenodo.17642991",
      "author": [
        { "@type": "Person", "@id": "https://orcid.org/0000-0003-3986-0510", "name": "Castro, L. J." }
      ],
      "datePublished": "2025-11-19"
    },
    {
      "@type": "PresentationDigitalDocument",
      "name": "Introducing ConnOSS - Connected Open-Source Software",
      "@id": "https://doi.org/10.5281/zenodo.18836442",
      "author": [
        { "@type": "Person", "@id": "https://orcid.org/0009-0008-7998-3965", "name": "Sefidbari, M." },
        { "@type": "Person", "@id": "https://orcid.org/0009-0005-7305-3052", "name": "Venkatesh, S." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0001-5844-3021", "name": "Gan, L." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0002-1435-0584", "name": "Jafarbigloo, A." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0001-9523-7227", "name": "Ferenz, S." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0003-1793-9615", "name": "Mathiak, B." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0003-1881-9172", "name": "Nieße, A." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0002-6767-5905", "name": "Werth, O." },
        { "@type": "Person", "@id": "https://orcid.org/0000-0003-3986-0510", "name": "Castro, L. J." }
      ],
      "datePublished": "2026-03-01"
    }
  ]
}
</script>