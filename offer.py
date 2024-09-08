import numpy as np
import pandas as pd

# Step 1: Define the Risks List
# -----------------------------

RISKS_LIST = [
    "Cancer", "Dermatological", "Endocrine", "Gastrointestinal", "Cardiovascular", 
    "Infectious Disease", "Immunological", "Kidney", "Hematological", "Musculoskeletal", 
    "Neurology", "Urological", "Psychiatric", "Ophthalmological", "Respiratory", 
    "Hepatological", "Gynaecological", "Andrological", "Endodontic", "Otolaryngological"
]

# Step 2: Function to Calculate Engagement Score
# ----------------------------------------------

def calculate_engagement_score(visits, treatment_type, feedback_score):
    """
    Calculate the engagement score based on:
    - Number of visits
    - Type of treatment
    - Patient's feedback score
    """
    treatment_weight = {
        "Cancer": 1.5, "Dermatological": 1.2, "Endocrine": 1.3, "Gastrointestinal": 1.4, 
        "Cardiovascular": 1.5, "Infectious Disease": 1.1, "Immunological": 1.2, "Kidney": 1.4, 
        "Hematological": 1.3, "Musculoskeletal": 1.3, "Neurology": 1.4, "Urological": 1.3, 
        "Psychiatric": 1.2, "Ophthalmological": 1.1, "Respiratory": 1.3, "Hepatological": 1.3, 
        "Gynaecological": 1.2, "Andrological": 1.2, "Endodontic": 1.1, "Otolaryngological": 1.1
    }
    
    engagement_score = (visits * 10) + (treatment_weight[treatment_type] * feedback_score)
    return min(engagement_score, 100)  # Cap at 100

# Step 3: Function to Dynamically Calculate Offer Amount
# ------------------------------------------------------

def calculate_offer_amount(engagement_score):
    """
    Calculate a dynamic offer percentage based on the engagement score.
    """
    if engagement_score >= 90:
        return 30
    elif 70 <= engagement_score < 90:
        return 25
    elif 50 <= engagement_score < 70:
        return 20
    else:
        return 15

# Step 4: Define Function to Generate Offer Paragraph
# ----------------------------------------------------

def generate_personalized_offer(patient_id, risk, engagement_score, patient_name):
    """
    Generate a personalized offer paragraph based on risk and engagement score.
    """
    # Offer details based on risk type
    offer_details = {
        "Cancer": "a complimentary cancer screening and a priority consultation with our oncologists",
        "Cardiovascular": "a free consultation with our leading cardiologist and a detailed heart health assessment",
        "Neurology": "a free brain health assessment and a personalized neurological care plan",
        "Dermatological": "a free skin check-up with our dermatology specialists",
        "Endocrine": "a comprehensive endocrine health evaluation",
        "Gastrointestinal": "an in-depth digestive health analysis",
        "Infectious Disease": "a specialized infectious disease consultation",
        "Immunological": "a detailed immune system health assessment",
        "Kidney": "a complete kidney function test and consultation",
        "Hematological": "a full blood health examination",
        "Musculoskeletal": "a thorough musculoskeletal assessment",
        "Urological": "a detailed urological health check",
        "Psychiatric": "a mental health screening with our psychiatric team",
        "Ophthalmological": "a complete eye health assessment",
        "Respiratory": "a full respiratory system check-up",
        "Hepatological": "a comprehensive liver function test",
        "Gynaecological": "a full women’s health check",
        "Andrological": "a complete men’s health assessment",
        "Endodontic": "a detailed dental and endodontic examination",
        "Otolaryngological": "a thorough ear, nose, and throat evaluation"
    }
    
    # Calculate dynamic offer percentage
    offer_percentage = calculate_offer_amount(engagement_score)
    
    # Select offer content
    offer_content = offer_details.get(risk, "an exclusive health check-up package tailored to your needs.")
    
    # Personalized statement based on engagement score
    if engagement_score >= 90:
        personalized_statement = f"We are impressed with your dedication to maintaining your health."
    elif 70 <= engagement_score < 90:
        personalized_statement = f"Your commitment to regular check-ups is commendable."
    elif 50 <= engagement_score < 70:
        personalized_statement = f"We appreciate your efforts in staying on top of your health."
    else:
        personalized_statement = f"Taking proactive steps in your health management is crucial."
    
    # Create the personalized offer paragraph
    offer_paragraph = (
        f"Dear {patient_name} (Patient ID: {patient_id}),\n\n"
        f"After a thorough review of your recent visits and medical history, we have identified a potential health concern related to {risk}. "
        f"{personalized_statement} With an engagement score of {engagement_score}, we want to ensure you receive the best possible care.\n\n"
        f"In light of this, we are pleased to offer you {offer_content} along with a **{offer_percentage}% discount** on any further treatments or diagnostic tests related to this condition. "
        f"Your well-being is our top priority, and this offer is designed to support your health journey and provide you with the care you need at a reduced cost.\n\n"
        f"To take advantage of this offer, please contact our care team at your earliest convenience, and we will be happy to assist you with the next steps. "
        f"We look forward to continuing to support your health and wellness journey.\n\n"
        f"Warm regards,\n"
        f"The Healthcare Team"
    )
    
    return offer_paragraph

# Step 5: Example Usage
# ---------------------

# Generate some dummy data
patients_data = {
    'patient_id': [101, 102, 103],
    'patient_name': ["John Doe", "Jane Smith", "Alex Johnson"],
    'risk': ["Cardiovascular", "Neurology", "Cancer"],
    'visits': [5, 8, 3],
    'feedback_score': [80, 70, 90]
}

df_patients = pd.DataFrame(patients_data)

# Calculate engagement scores for each patient
df_patients['engagement_score'] = df_patients.apply(
    lambda x: calculate_engagement_score(x['visits'], x['risk'], x['feedback_score']), axis=1)

# Generate personalized offers
df_patients['personalized_offer'] = df_patients.apply(
    lambda x: generate_personalized_offer(x['patient_id'], x['risk'], x['engagement_score'], x['patient_name']), axis=1)

# Display the personalized offers
for offer in df_patients['personalized_offer']:
    print(offer)
    print("\n" + "="*80 + "\n")
