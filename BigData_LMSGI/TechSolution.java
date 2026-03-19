```java
/**
 * Filename: XMLToHTMLTransformer.java
 *
 * Description: This Java class is designed to transform an input XML document into an HTML document using XSLT.
 */

import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.stream.StreamSource;
import java.io.File;

public class XMLToHTMLTransformer {

    /**
     * Method to transform an XML file into an HTML file based on the provided XSL style sheet.
     *
     * @param xmlFile The input XML file that needs to be transformed.
     * @param xslFile The XSLT stylesheet used for transforming the XML document.
     * @throws Exception If there is any error during transformation or file reading.
     */
    public void transformXMLToHTML(File xmlFile, File xslFile) throws Exception {
        // Create a TransformerFactory object
        TransformerFactory transformerFactory = TransformerFactory.newInstance();

        // Load the XSLT stylesheet from the given file
        Transformer transformer = transformerFactory.newTransformer(new StreamSource(xslFile));

        // Perform the transformation and write the result to an HTML file
        transformer.transform(new javax.xml.transform.stream.StreamSource(xmlFile), new javax.xml.transform.stream.StreamResult(new File("output.html")));
    }

    /**
     * Main method for testing purposes.
     *
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        // Example usage
        XMLToHTMLTransformer transformer = new XMLToHTMLTransformer();
        
        try {
            File xmlFile = new File("input.xml");
            File xslFile = new File("style.xsl");

            // Transform the XML file to HTML using the provided XSLT stylesheet
            transformer.transformXMLToHTML(xmlFile, xslFile);
            
            System.out.println("Transformation completed. Check 'output.html' for results.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

Esta solución Java permite transformar un archivo XML en HTML utilizando un estilo XSLT. El método `transformXMLToHTML` lleva a cabo la transformación y el resultado se guarda en un archivo HTML denominado "output.html".