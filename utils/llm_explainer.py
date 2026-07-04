from groq import Groq
from dotenv import load_dotenv
import os

# ---------------------------------------
# Load Environment Variables
# ---------------------------------------

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------------------------------
# Transaction Type Descriptions
# ---------------------------------------

TRANSACTION_TYPES = {

    "CASH_IN": {
        "title": "Cash Deposit",
        "description": (
            "This transaction represents a cash deposit into an account. "
            "Cash deposits generally increase the account balance and are "
            "typically made by customers or authorized third parties."
        )
    },

    "CASH_OUT": {
        "title": "Cash Withdrawal",
        "description": (
            "This transaction represents a withdrawal of funds from an account. "
            "Cash withdrawals reduce the available account balance and should "
            "normally be authorized by the account holder."
        )
    },

    "TRANSFER": {
        "title": "Funds Transfer",
        "description": (
            "This transaction transfers money from one account to another. "
            "Transfers may occur between customers, businesses or financial "
            "institutions."
        )
    },

    "PAYMENT": {
        "title": "Merchant Payment",
        "description": (
            "This transaction represents a payment made for goods, services, "
            "subscriptions or utility bills."
        )
    },

    "DEBIT": {
        "title": "Direct Debit",
        "description": (
            "This transaction deducts money directly from the customer's "
            "account following an authorized instruction."
        )
    }

}

# ---------------------------------------
# Recommendations
# ---------------------------------------

RECOMMENDATIONS = {

    "CASH_IN": {

        "Fraud":
            "Verify the source of the deposited funds, perform Anti-Money Laundering (AML) checks and review supporting documentation before crediting the account.",
        "Not Fraud":
            "The transaction may proceed under normal banking procedures while maintaining routine monitoring."
    },

    "CASH_OUT": {

        "Fraud":
            "Confirm that the withdrawal was authorized by the account holder before releasing the funds.",
        "Not Fraud":
            "The withdrawal appears consistent with the available information. Continue standard account monitoring."
    },

    "TRANSFER": {

        "Fraud":
            "Verify the recipient account and temporarily hold the transfer until additional verification is completed.",
        "Not Fraud":
            "The transfer appears legitimate based on the model prediction. Continue routine monitoring."
    },

    "PAYMENT": {

        "Fraud":
            "Verify the payment destination before completing the transaction and notify the customer if necessary.",
        "Not Fraud":
            "The payment appears legitimate and can proceed according to normal banking procedures."
    },

    "DEBIT": {

        "Fraud":
            "Confirm that the debit instruction was authorized by the account owner before processing.",
        "Not Fraud":
            "The debit appears consistent with normal account activity. Continue standard monitoring."
    }

}

# ---------------------------------------
# Risk Level
# ---------------------------------------

def get_risk_level(score):

    if score >= 90:
        return "Critical"

    elif score >= 70:
        return "High"

    elif score >= 40:
        return "Medium"

    else:
        return "Low"

# ---------------------------------------
# Confidence Level
# ---------------------------------------

def get_confidence(score):

    if score >= 90:
        return "Very High"

    elif score >= 70:
        return "High"

    elif score >= 50:
        return "Moderate"

    else:
        return "Low"

# ---------------------------------------
# Format Money
# ---------------------------------------

def naira(value):
    """
    Format currency consistently throughout the report.
    """

    return f"₦{value:,.2f}"

# ---------------------------------------
# Prompt Builder
# ---------------------------------------

def build_prompt(transaction, prediction, risk_score):

    tx_type = transaction["transaction_type"]

    tx_info = TRANSACTION_TYPES.get(
        tx_type,
        {
            "title": "Financial Transaction",
            "description": "A financial transaction."
        }
    )

    recommendation = RECOMMENDATIONS.get(
        tx_type,
        {}
    ).get(
        prediction,
        "Continue routine monitoring."
    )

    risk_level = get_risk_level(risk_score)

    confidence = get_confidence(risk_score)

    amount = naira(transaction["transaction_amount"])

    sender_balance = naira(
        transaction["sender_balance_before"]
    )

    receiver_balance = naira(
        transaction["receiver_balance_before"]
    )

    prompt = f"""
You are a Senior Financial Fraud Analyst working for a Nigerian commercial bank.

Your responsibility is to explain the result produced by a machine learning fraud detection model.

The audience is a bank employee, compliance officer or customer.

======================================================
STRICT RULES
======================================================

1. NEVER invent information.

2. NEVER guess hidden reasons.

3. NEVER mention features that are not provided.

4. NEVER say the model detected unusual behaviour unless Prediction = Fraud.

5. NEVER contradict the prediction.

6. NEVER use "$", "USD", "US Dollars" or any foreign currency.

7. ALL money is in Nigerian Naira (₦).

8. NEVER change any amount.

9. Do not mention probabilities that were not supplied.

10. Do not claim certainty.

11. Treat the machine learning prediction as the only prediction available.

12. Base every sentence ONLY on the supplied transaction information.

======================================================
TRANSACTION DETAILS
======================================================

Transaction Category

{tx_info["title"]}

Transaction Description

{tx_info["description"]}

Transaction Amount

{amount}

Transaction Type

{tx_type}

Transaction Hour

{transaction["transaction_hour"]}:00

Sender Balance Before

{sender_balance}

Receiver Balance Before

{receiver_balance}

Machine Learning Prediction

{prediction}

Fraud Risk Score

{risk_score:.2f}%

Risk Level

{risk_level}

Confidence

{confidence}

Recommendation

{recommendation}

======================================================
HOW TO WRITE THE REPORT
======================================================

Write FIVE short sections.

SECTION 1
Title:
Prediction Summary

Explain what "{prediction}" means.

If prediction is "Not Fraud",
say that the model indicates a low likelihood of fraud based on the available information.

If prediction is "Fraud",
say that the transaction should be reviewed because the model identified characteristics associated with fraudulent activity.

Never say fraud is confirmed.

------------------------------------------------------

SECTION 2

Title:
Transaction Summary

Briefly explain the purpose of this transaction type using the supplied description.

Mention:

• Amount

• Transaction Type

• Transaction Hour

Do NOT add anything else.

------------------------------------------------------

SECTION 3

Title:
Risk Assessment

Explain what the Risk Score means.

If Risk Level is Low

say the transaction presents relatively low fraud risk.

If Medium

say additional monitoring may be appropriate.

If High

say additional verification is recommended.

If Critical

say immediate review is recommended.

------------------------------------------------------

SECTION 4

Title:
Recommended Action

Use ONLY the supplied recommendation.

Do NOT rewrite it into something different.

------------------------------------------------------

SECTION 5

Title:
Conclusion

Provide one professional concluding sentence.

Maximum response length:
170 words.

The report must sound like it was written by a banking fraud analyst.

Never use markdown.

Never use bullet points.

Never use tables.

Never use emojis.
"""

    return prompt

# ---------------------------------------
# AI Fraud Report Generator
# ---------------------------------------

def explain_prediction(transaction, prediction, risk_score):

    prompt = build_prompt(
        transaction=transaction,
        prediction=prediction,
        risk_score=risk_score
    )

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            temperature=0.1,

            max_tokens=350,

            top_p=0.9,

            messages=[

                {
                    "role": "system",
                    "content":
                    """
You are a Senior Fraud Risk Analyst working for a Nigerian commercial bank.

Your responsibility is to explain machine learning predictions.

You NEVER invent information.

You NEVER contradict the prediction.

You NEVER assume hidden behaviour.

You NEVER fabricate reasons.

All money is Nigerian Naira (₦).

Never use $, USD or Dollars.

Always produce professional banking reports.

Use only the supplied information.
                    """
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ]

        )

        report = response.choices[0].message.content.strip()

        # Safety replacement in case the model slips
        report = (
            report.replace("₦", "₦")
                  .replace("USD", "Nigerian Naira")
                  .replace("US Dollars", "Nigerian Naira")
                  .replace("dollars", "Naira")
                  .replace("Dollar", "Naira")
        )

        return report

    except Exception:

        tx_type = transaction["transaction_type"]

        recommendation = RECOMMENDATIONS.get(
            tx_type,
            {}
        ).get(
            prediction,
            "Continue routine monitoring."
        )

        risk_level = get_risk_level(risk_score)

        tx_title = TRANSACTION_TYPES.get(
            tx_type,
            {
                "title": tx_type,
                "description": "Financial transaction."
            }
        )

        if prediction == "Fraud":

            return f"""
Prediction Summary

The machine learning model classified this {tx_title['title'].lower()} as potentially fraudulent.
This prediction indicates that the transaction contains characteristics associated with fraudulent activity.
It should be reviewed before further processing.

Transaction Summary

Transaction Type: {tx_type}

Transaction Amount: {naira(transaction['transaction_amount'])}

Transaction Time: {transaction['transaction_hour']}:00

Risk Assessment

The calculated fraud risk score is {risk_score:.2f}% which corresponds to a {risk_level} risk level.
This does not confirm fraud but indicates that additional verification is recommended.

Recommended Action

{recommendation}

Conclusion

The transaction should remain under review until the recommended verification procedures have been completed.
"""

        else:

            return f"""
Prediction Summary

The machine learning model classified this transaction as Not Fraud.
Based on the available transaction information, the model indicates a low likelihood of fraudulent activity.

Transaction Summary

Transaction Type: {tx_type}

Transaction Amount: {naira(transaction['transaction_amount'])}

Transaction Time: {transaction['transaction_hour']}:00

Risk Assessment

The calculated fraud risk score is {risk_score:.2f}% which corresponds to a {risk_level} risk level.
The transaction appears consistent with normal activity based on the information available to the model.

Recommended Action

{recommendation}

Conclusion

The transaction may proceed in accordance with the bank's standard operating procedures while continuing routine monitoring.
"""