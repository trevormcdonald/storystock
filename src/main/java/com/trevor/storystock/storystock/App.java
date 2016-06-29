package com.trevor.storystock.storystock;

import java.io.StringReader;

import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

import de.l3s.boilerpipe.BoilerpipeExtractor;
import de.l3s.boilerpipe.BoilerpipeProcessingException;
import de.l3s.boilerpipe.extractors.*;
import de.l3s.boilerpipe.sax.BoilerpipeSAXInput;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
    	String html = args[0];
    	try {
            return getText(new BoilerpipeSAXInput(new InputSource(
                    new StringReader(html))).getTextDocument());
        } catch (SAXException e) {
            throw new BoilerpipeProcessingException(e);
        }
        System.out.println( "Hello World!" );
    }
}
