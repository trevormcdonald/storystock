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
    	getText(html);
    }
    /***
     * When given the address of an article, returns the main body.
     * @param html String, address of the article
     * @return String that is the main content of the article.
     */
    public static String getText(String html){
    	String content;
    	try {
			content= ArticleExtractor.INSTANCE.getText(html);
			return content;
		} catch (BoilerpipeProcessingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return "";
		}
    }
}
