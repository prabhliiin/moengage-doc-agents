import os
from gemini_api import get_gemini_response
from scraper import extract_text_from_url


def rewrite_article(url, suggestions_text):
    """
    Rewrites an article based on improvement suggestions
    
    Args:
        url (str): URL of the article to rewrite
        suggestions_text (str): Improvement suggestions from analysis
    
    Returns:
        str: The revised article text
    """
    try:
        print(f"Extracting original content from: {url}")
        original = extract_text_from_url(url)
        
        if not original or len(original.strip()) == 0:
            raise ValueError("No content extracted from URL")
        
        print("Preparing rewrite prompt...")
        prompt = f"""You are an expert technical documentation editor specializing in marketing content.

Your task is to completely rewrite the following article by applying the improvement suggestions provided.

ORIGINAL ARTICLE:
{original[:10000]}

IMPROVEMENT SUGGESTIONS TO APPLY:
{suggestions_text}

REWRITING INSTRUCTIONS:
1. Maintain all key information and facts from the original
2. Apply ALL the readability suggestions (simplify language, shorter sentences, active voice)
3. Restructure content with clear headings and logical flow
4. Add concrete examples where suggested
5. Use customer-focused, action-oriented language
6. Follow professional writing standards
7. Include clear calls-to-action
8. Format as clean, readable markdown

Please provide the complete rewritten article:"""

        print("Generating revised content...")
        revised = get_gemini_response(prompt)
        
        if not revised:
            raise ValueError("No response received from Gemini API")
        
        # Ensure output directory exists
        output_dir = "examples"
        os.makedirs(output_dir, exist_ok=True)
        
        # Save to file
        output_path = os.path.join(output_dir, "revised.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(revised)
        
        print(f"Revised article saved to {output_path}")
        print(f"Original length: {len(original)} characters")
        print(f"Revised length: {len(revised)} characters")
        
        return revised
        
    except Exception as e:
        error_msg = f"Error rewriting article: {str(e)}"
        print(error_msg)
        return error_msg


def rewrite_from_analysis_file(url, analysis_json_path="examples/report.json"):
    """
    Convenience function to rewrite using suggestions from analysis file
    
    Args:
        url (str): URL of the article to rewrite
        analysis_json_path (str): Path to the analysis JSON file
    
    Returns:
        str: The revised article text
    """
    try:
        import json
        
        with open(analysis_json_path, "r", encoding="utf-8") as f:
            analysis_data = json.load(f)
        
        suggestions = analysis_data.get("gemini_analysis", "")
        if not suggestions:
            raise ValueError("No analysis found in the JSON file")
        
        return rewrite_article(url, suggestions)
        
    except Exception as e:
        error_msg = f"Error reading analysis file: {str(e)}"
        print(error_msg)
        return error_msg


# Example usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python rewriter.py <URL> [suggestions_text]")
        print("  python rewriter.py <URL> --from-analysis")
        sys.exit(1)
    
    url = sys.argv[1]
    
    if len(sys.argv) == 3 and sys.argv[2] == "--from-analysis":
        # Use suggestions from existing analysis file
        result = rewrite_from_analysis_file(url)
    elif len(sys.argv) == 3:
        # Use provided suggestions
        suggestions = sys.argv[2]
        result = rewrite_article(url, suggestions)
    else:
        # Use suggestions from existing analysis file as default
        result = rewrite_from_analysis_file(url)
    
    if not result.startswith("❌"):
        print("Rewrite completed successfully!")