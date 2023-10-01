# from transformers import BartTokenizer, BartForConditionalGeneration
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer

# import re

# legal_jargon_dictionary = {
    # "plaintiff": "complainant",
    # "defendant": "accused",
    # "judgment": "decision",
    # "lawsuit": "legal case or legal proceeding",
    # "alleging": "claiming",
    # "breach": "violation",
    # # "postnuptial": "Marriage",
    # # "postnuptial agreement": "Marriage agreement",
    # "plaintiff's attorney": "complainant's lawyer",
    # "defendant's attorney": "accused's lawyer",
    # "courtroom": "court",
    # "testimony": "evidence",
    # "subpoena": "legal summons",
    # "verdict": "decision",
    # "injunction": "court order",
    # "breach of contract": "contract violation",
    # "affidavit": "sworn statement",
    # "allegation": "claim",
    # "liability": "legal responsibility",
    # "witness": "observer",
    # "hearsay": "secondhand information",
    # "arbitration": "mediation",
    # "plaintiff's claim": "complainant's assertion",
    # "defendant's response": "accused's reply",
    # "legal brief": "legal document",
    # "pretrial conference": "pre-hearing meeting",
    # "adjudication": "decision-making",
    # "jury selection": "jury picking",
    # "voir dire": "jury selection",
    # "substantive law": "law dealing with rights and duties",
    # "procedural law": "law dealing with legal procedures",
    # "amicus curiae": "friend of the court",
    # "ex parte": "one party",
    # "pro se": "self-represented",
    # "tort": "civil wrong",
    # "mens rea": "guilty mind",
    # "actus reus": "guilty act",
    # "judicial review": "court examination",
    # "affirmative defense": "assertive defense",
    # "statute of limitations": "time limit for legal action",
    # "beyond a reasonable doubt": "very certain",
    # "class action lawsuit": "group lawsuit",
    # "sua sponte": "on its own motion",
    # "voir dire examination": "jury selection questioning",
    # "habeas corpus": "produce the body",
    # "en banc": "full bench",
    # "rebuttal": "contradiction",
    # "remand": "send back",
    # "quid pro quo": "something for something",
    # "writ of certiorari": "order to review",
    # "amicable": "friendly",
    # "perjury": "false statement under oath",
    # "jurisprudence": "philosophy of law",
    # "discovery": "evidence collection",
    # "impeachment of a witness": "discrediting a witness",
    # "preamble": "introduction",
    # "estoppel": "forbidden",
    # "parole": "conditional release",
    # "caveat emptor": "buyer beware",
    # "statutory law": "written law",
    # "voir dire challenge": "jury selection objection",
    # "deposition": "statement under oath",
    # "exclusionary rule": "evidence exclusion",
    # "quash": "nullify",
    # "interlocutory order": "interim decision",
    # "mitigating circumstances": "reducing factors",
    # "collateral estoppel": "issue preclusion",
    # "res ipsa loquitur": "the thing speaks for itself",
    # "voir dire panel": "jury selection group",
    # "discovery dispute": "evidence disagreement",
    # "in propria persona": "in one's own person",
    # "replevin": "recovery of goods",
    # "estoppel by deed": "binding agreement",
    # "juror misconduct": "jury member wrongdoing",
    # "promissory estoppel": "reliance on a promise",
    # "prosecutorial misconduct": "prosecutor wrongdoing",
    # "voir dire process": "jury selection procedure",
    # "amicable settlement": "friendly resolution",
    # "recuse": "disqualify",
    # "judicial discretion": "judge's decision-making",
    # "voir dire challenge for cause": "jury selection objection based on bias",
    # "ad litem": "for the purpose of the lawsuit",
    # "in forma pauperis": "in the form of a pauper",
    # "peremptory challenge": "dismissing a juror without reason",
    # "burden of proof": "responsibility to prove",
    # "rebuttable presumption": "presumption that can be challenged",
    # "res gestae": "things done",
    # "voir dire questionnaire": "jury selection survey",
    # "affirmative action": "positive discrimination",
    # "estoppel certificate": "binding certificate",
    # "judicial foreclosure": "court-ordered property sale",
    # "voir dire examination of prospective jurors": "questioning potential jurors",
    # "affidavit of service": "sworn statement of delivery",
    # "interlocutory appeal": "interim case appeal",
    # "judicial review of administrative action": "court examination of agency decisions",
    # "voir dire voir dire voir dire": "jury selection process",
    # "prima facie": "at first sight",
    # "voir dire jury selection": "jury member questioning and selection",
    # "in camera": "in private",
    # "strict liability": "absolute responsibility",
    # "voir dire challenge based on group bias": "jury selection objection based on bias",
    # "acquittal": "not guilty verdict",
    # "judicial estoppel": "court-enforced consistency",
    # "voir dire challenge based on race or ethnicity": "jury selection objection based on bias",
# }

# # Load the BART model and tokenizer
# model_name = "facebook/bart-large-cnn"
# tokenizer = BartTokenizer.from_pretrained(model_name)
# model = BartForConditionalGeneration.from_pretrained(model_name)

# import textwrap
# # from transformers import BartTokenizer, BartForConditionalGeneration

# def summarize_legal_document(input_text, tokenizer, model, max_input_length=1024, max_summary_length=400):
#     try:
#         # Initialize an empty list to store the summaries
#         summaries = []

#         # Tokenize the input text
#         input_ids = tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=max_input_length, truncation=True)

#         # Check if the input exceeds the maximum token limit
#         if len(input_ids[0]) > model.config.max_position_embeddings:
#             # If it exceeds the limit, split the input into segments
#             input_segments = [input_ids[:, i:i+max_input_length] for i in range(0, len(input_ids[0]), max_input_length)]

#             for input_segment in input_segments:
#                 # Generate the summary for the segment
#                 summary_ids = model.generate(input_segment, max_length=max_summary_length, min_length=100, num_beams=4, length_penalty=2.0, early_stopping=True)

#                 # Decode the summary
#                 summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#                 # Add the summary to the list
#                 summaries.append(summary)

#         else:
#             # If the input doesn't exceed the limit, generate the summary directly
#             summary_ids = model.generate(input_ids, max_length=max_summary_length, min_length=100, num_beams=4, length_penalty=2.0, early_stopping=True)

#             # Decode the summary
#             summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#             # Add the summary to the list
#             summaries.append(summary)

#         # Join the summaries to create the final summarized document
#         formatted_summary = "\n".join(textwrap.wrap('\n'.join(summaries), width=80))

#         return formatted_summary

#     except Exception as e:
#         return str(e)

# # Example usage
# # model_name = "facebook/bart-large-cnn"
# # tokenizer = BartTokenizer.from_pretrained(model_name)
# # model = BartForConditionalGeneration.from_pretrained(model_name)

# input_text = """IN THE CIRCUIT COURT OF THE STATE OF OREGON
# FOR THE COUNTY OF MULTNOMAH

# Plaintiff,
# v.
# Defendant.

# CASE NO: 12345

# COMPLAINT FOR BREACH OF CONTRACT

# COMES NOW the Plaintiff, [Your Name], and for the Complaint against the Defendant, [Defendant's Name], alleges as follows:

# 1. Parties and Jurisdiction

# 1.1 Plaintiff, [Your Name], is an individual residing at [Your Address], Multnomah County, Oregon.

# 1.2 Defendant, [Defendant's Name], is a business entity located at [Defendant's Address], Multnomah County, Oregon.

# 1.3 This Court has jurisdiction over the subject matter of this action and over the parties hereto.

# 2. Breach of Contract

# 2.1 On or about [Date], Plaintiff and Defendant entered into a written contract (the "Contract") whereby Defendant agreed to provide [Description of Services] to Plaintiff in exchange for payment of [Amount] by Plaintiff.

# 2.2 Plaintiff performed all obligations under the Contract, including making the required payment.

# 2.3 Defendant, however, failed to perform its obligations under the Contract by [Specify Breach].

# 3. Damages

# 3.1 As a direct and proximate result of Defendant's breach of the Contract, Plaintiff has suffered damages in the amount of [Amount], which includes [Itemized List of Damages].

# WHEREFORE, Plaintiff prays for judgment against Defendant in the amount of [Amount], plus interest, costs, and such other relief as the Court deems just and proper.

# DATED this [Date] day of [Month], 20[Year].

# Piyush
# Piyush Kumar Dewangan
# Durg
# Ward 6 Sindhiya Nagar Durg
# 9509586085

# """

# # Call the summarize_legal_document function with the input text
# result = summarize_legal_document(input_text, tokenizer, model)

# # Print or use the result as needed
# # print(result)

# def clean_ocr_text(ocr_text):
#     # Remove special characters and symbols (keep alphanumeric characters, spaces, and periods)
#     cleaned_text = re.sub(r'[^\w\s.]', '', ocr_text)

#     # Normalize whitespace (replace multiple spaces with a single space)
#     cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

#     # Remove extra periods (full stops) within sentences (e.g., "Mr. Smith" should remain)
#     cleaned_text = re.sub(r'(?<=[A-Za-z])\.(?=[A-Za-z])', '', cleaned_text)

#     # Remove starting numbers with periods (e.g., "1.2")
#     cleaned_text = re.sub(r'^\d+\.\d+\s*', '', cleaned_text)

#     return cleaned_text

# # Example usage
# ocr_input = result
# cleaned_text = clean_ocr_text(ocr_input)
# # print(cleaned_text)


# def replace_legal_jargon(input_text, jargon_dict):
#     words = input_text.split()
#     modified_words = []

#     for word in words:
#         word_stripped = word.strip('.,?!()[]{}"\'')

#         if word_stripped.lower() in jargon_dict:
#             modified_words.append(jargon_dict[word_stripped.lower()])
#         else:
#             modified_words.append(word)

#     modified_text = ' '.join(modified_words)
#     return modified_text

# # Example legal document-related input
# input_text = cleaned_text

# # Replace legal jargon terms
# modified_text = replace_legal_jargon(input_text, legal_jargon_dictionary)

# print("Modified Text:")
# print(modified_text)

from transformers import BartTokenizer, BartForConditionalGeneration
import re
import textwrap

legal_jargon_dictionary = {
    "plaintiff": "complainant",
    "defendant": "accused",
    "judgment": "decision",
    "lawsuit": "legal case or legal proceeding",
    "alleging": "claiming",
    "breach": "violation",
    # "postnuptial": "Marriage",
    # "postnuptial agreement": "Marriage agreement",
    "plaintiff's attorney": "complainant's lawyer",
    "defendant's attorney": "accused's lawyer",
    "courtroom": "court",
    "testimony": "evidence",
    "subpoena": "legal summons",
    "verdict": "decision",
    "injunction": "court order",
    "breach of contract": "contract violation",
    "affidavit": "sworn statement",
    "allegation": "claim",
    "liability": "legal responsibility",
    "witness": "observer",
    "hearsay": "secondhand information",
    "arbitration": "mediation",
    "plaintiff's claim": "complainant's assertion",
    "defendant's response": "accused's reply",
    "legal brief": "legal document",
    "pretrial conference": "pre-hearing meeting",
    "adjudication": "decision-making",
    "jury selection": "jury picking",
    "voir dire": "jury selection",
    "substantive law": "law dealing with rights and duties",
    "procedural law": "law dealing with legal procedures",
    "amicus curiae": "friend of the court",
    "ex parte": "one party",
    "pro se": "self-represented",
    "tort": "civil wrong",
    "mens rea": "guilty mind",
    "actus reus": "guilty act",
    "judicial review": "court examination",
    "affirmative defense": "assertive defense",
    "statute of limitations": "time limit for legal action",
    "beyond a reasonable doubt": "very certain",
    "class action lawsuit": "group lawsuit",
    "sua sponte": "on its own motion",
    "voir dire examination": "jury selection questioning",
    "habeas corpus": "produce the body",
    "en banc": "full bench",
    "rebuttal": "contradiction",
    "remand": "send back",
    "quid pro quo": "something for something",
    "writ of certiorari": "order to review",
    "amicable": "friendly",
    "perjury": "false statement under oath",
    "jurisprudence": "philosophy of law",
    "discovery": "evidence collection",
    "impeachment of a witness": "discrediting a witness",
    "preamble": "introduction",
    "estoppel": "forbidden",
    "parole": "conditional release",
    "caveat emptor": "buyer beware",
    "statutory law": "written law",
    "voir dire challenge": "jury selection objection",
    "deposition": "statement under oath",
    "exclusionary rule": "evidence exclusion",
    "quash": "nullify",
    "interlocutory order": "interim decision",
    "mitigating circumstances": "reducing factors",
    "collateral estoppel": "issue preclusion",
    "res ipsa loquitur": "the thing speaks for itself",
    "voir dire panel": "jury selection group",
    "discovery dispute": "evidence disagreement",
    "in propria persona": "in one's own person",
    "replevin": "recovery of goods",
    "estoppel by deed": "binding agreement",
    "juror misconduct": "jury member wrongdoing",
    "promissory estoppel": "reliance on a promise",
    "prosecutorial misconduct": "prosecutor wrongdoing",
    "voir dire process": "jury selection procedure",
    "amicable settlement": "friendly resolution",
    "recuse": "disqualify",
    "judicial discretion": "judge's decision-making",
    "voir dire challenge for cause": "jury selection objection based on bias",
    "ad litem": "for the purpose of the lawsuit",
    "in forma pauperis": "in the form of a pauper",
    "peremptory challenge": "dismissing a juror without reason",
    "burden of proof": "responsibility to prove",
    "rebuttable presumption": "presumption that can be challenged",
    "res gestae": "things done",
    "voir dire questionnaire": "jury selection survey",
    "affirmative action": "positive discrimination",
    "estoppel certificate": "binding certificate",
    "judicial foreclosure": "court-ordered property sale",
    "voir dire examination of prospective jurors": "questioning potential jurors",
    "affidavit of service": "sworn statement of delivery",
    "interlocutory appeal": "interim case appeal",
    "judicial review of administrative action": "court examination of agency decisions",
    "voir dire voir dire voir dire": "jury selection process",
    "prima facie": "at first sight",
    "voir dire jury selection": "jury member questioning and selection",
    "in camera": "in private",
    "strict liability": "absolute responsibility",
    "voir dire challenge based on group bias": "jury selection objection based on bias",
    "acquittal": "not guilty verdict",
    "judicial estoppel": "court-enforced consistency",
    "voir dire challenge based on race or ethnicity": "jury selection objection based on bias",
}

def process_legal_document(ocr_input):
    try:
        # Load the BART model and tokenizer
        model_name = "facebook/bart-large-cnn"
        tokenizer = BartTokenizer.from_pretrained(model_name)
        model = BartForConditionalGeneration.from_pretrained(model_name)

        # Define the clean_ocr_text function
        def clean_ocr_text(ocr_text):
            cleaned_text = re.sub(r'[^\w\s.]', '', ocr_text)
            cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
            cleaned_text = re.sub(r'(?<=[A-Za-z])\.(?=[A-Za-z])', '', cleaned_text)
            cleaned_text = re.sub(r'^\d+\.\d+\s*', '', cleaned_text)
            return cleaned_text

        # Define the replace_legal_jargon function
        def replace_legal_jargon(input_text, jargon_dict):
            words = input_text.split()
            modified_words = []

            for word in words:
                word_stripped = word.strip('.,?!()[]{}"\'')

                if word_stripped.lower() in jargon_dict:
                    modified_words.append(jargon_dict[word_stripped.lower()])
                else:
                    modified_words.append(word)

            modified_text = ' '.join(modified_words)
            return modified_text

        # Clean the OCR text
        cleaned_text = clean_ocr_text(ocr_input)

        # Summarize the cleaned text
        input_text = "summarize: " + cleaned_text
        input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(input_ids, max_length=400, min_length=100, num_beams=4, length_penalty=2.0, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        # Replace legal jargon terms
        modified_text = replace_legal_jargon(summary, legal_jargon_dictionary)

        return modified_text

    except Exception as e:
        return str(e)

# # Example usage
# ocr_input = """
#              // Provide text here
# """

# modified_text = process_legal_document(ocr_input)

# print("Modified Text:")
# print(modified_text)
