CONVERSATION = {
    "start": {
        "text": "How would you like to proceed?",
        "buttons": [
            {"label": "Learn about fraud protection", "next": "learn"},
            {"label": "Business solutions", "next": "business"},
            {"label": "Just browsing", "next": "browse"},
        ]
    },

    "learn": {
        "text": "Fraud protection helps prevent scams, identity theft, and misuse.",
        "buttons": [
            {"label": "Common fraud types", "next": "types"},
            {"label": "Talk to expert", "next": "fallback"},
        ]
    },

    "business": {
        "text": "Businesses face payment fraud, fake accounts, and data misuse.",
        "buttons": [
            {"label": "Monitoring & alerts", "next": "monitoring"},
            {"label": "Book appointment", "next": "appointment"},
        ]
    },

    "browse": {
        "text": "Feel free to explore or talk to an expert anytime.",
        "buttons": [
            {"label": "Talk to human", "next": "fallback"},
            {"label": "End chat", "next": "end"},
        ]
    },

    "types": {
        "text": "Common fraud includes phishing, fake links, and social engineering.",
        "buttons": [
            {"label": "Book appointment", "next": "appointment"},
            {"label": "End chat", "next": "end"},
        ]
    },

    "monitoring": {
        "text": "Monitoring systems detect unusual behavior early.",
        "buttons": [
            {"label": "Book appointment", "next": "appointment"},
            {"label": "End chat", "next": "end"},
        ]
    },

    "appointment": {
        "text": "An expert will contact you. Please share your details.",
        "buttons": []
    }
}
