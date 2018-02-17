# Ontology

Semantic Web

*"Applications of Semantic Web technologies"* are defined by using metadata in a metadata-specific way.

1. Web Data Exchange and Syndication
   * Endowing Web Data with Metadata
   * Vocabularies
2. Semantic Wikis
3. Semantic Portals
4. Semantic Metadata in Data Formats
5. Semantic Web in Life Sciences
6. Ontologies for Standardizations
7. RIF Applications, `W3C RIF working group`
8. Toward Future Applications

> "Foundations of Semantic Web Technologies" - Pascal Hitzler, Markus Krtzsch, Sebastian Rudolph

| domain     | sub-domain | purl |
|------------|------------|------|
| **socio**  | water      | [purl.org/socio/water](http://purl.org/socio/water) |
| **water**  | wsn        | [purl.org/water/wsn](http://purl.org/water/wsn)     |
| **water**  | lake       | [purl.org/water/lake](http://purl.org/water/lake)   |

## Demo

### SWIM [link](http://www.semanticwater.com/SWIM)

```xml
<?xml version="1.0"?>
<rdf:RDF xmlns="http://www.semanticwater.com/SWIM#"
     xml:base="http://www.semanticwater.com/SWIM"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:xml="http://www.w3.org/XML/1998/namespace"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#">
     
     ...
     
</rdf:RDF>
```

| Asset        | Graph |
|--------------|-------|
| ControlAsset | ![SWIM-Asset.ControlAsset](https://raw.githubusercontent.com/quanpan302/phd/master/docker/ontology/water/SemanticWater/SWIM.Asset.ControlAsset.png) |
| FixedAsset   | ![SWIM-Asset.FixedAsset](https://raw.githubusercontent.com/quanpan302/phd/master/docker/ontology/water/SemanticWater/SWIM.Asset.FixedAsset.png) |
| Plant        | ![SWIM-Asset.Plant](https://raw.githubusercontent.com/quanpan302/phd/master/docker/ontology/water/SemanticWater/SWIM.Asset.Plant.png) |
| Sensor       | ![SWIM-Asset.Sensor](https://raw.githubusercontent.com/quanpan302/phd/master/docker/ontology/water/SemanticWater/SWIM.Asset.Sensor.png) |

### WISDOM [link](http://www.semanticwater.com/WISDOM)

```xml
<?xml version="1.0"?>
<rdf:RDF xmlns="http://www.semanticwater.com/WISDOM#"
     xml:base="http://www.semanticwater.com/WISDOM"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:ns="http://creativecommons.org/ns#"
     xmlns:swrlb="http://www.w3.org/2003/11/swrlb#"
     xmlns:swrl="http://www.w3.org/2003/11/swrl#"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:swrla="http://swrl.stanford.edu/ontologies/3.3/swrla.owl#"
     xmlns:ssn="http://purl.oclc.org/NET/ssnx/ssn#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:terms="http://purl.org/dc/terms/"
     xmlns:xml="http://www.w3.org/XML/1998/namespace"
     xmlns:DUL="http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#"
     xmlns:vann="http://purl.org/vocab/vann/"
     xmlns:dc="http://purl.org/dc/elements/1.1/">
     
     ...
     
</rdf:RDF>
```

| Object          | Graph |
|-----------------|-------|
| Agent           | ![WISDOM-Object.Agent](https://raw.githubusercontent.com/quanpan302/phd/master/docker/ontology/water/SemanticWater/WISDOM-Object.Agent.png) |
| Physical Object | ![WISDOM-Object.Physical Object](https://raw.githubusercontent.com/quanpan302/phd/master/docker/ontology/water/SemanticWater/WISDOM-Object.PhysicalObject.png) |
| SocialObject    | ![WISDOM-Object.SocialObject](https://raw.githubusercontent.com/quanpan302/phd/master/docker/ontology/water/SemanticWater/WISDOM-Object.SocialObject.png) |

### DBpedia [link](http://wiki.dbpedia.org)

### NASA sweet [link](https://sweet.jpl.nasa.gov)
