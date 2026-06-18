import random

class ReplyEngine:
    def __init__(self):
        self.replies = {
            "added": [
                "Added. If this song flops, that’s on you.",
                "Boom. Added. Try not to ruin the queue again.",
                "Song added. My taste is still better than yours.",
                "Done. Don’t say I never do anything for you.",
            ],
            "skipped": [
                "Skipped. That song was mid anyway.",
                "Next. I saved your ears.",
                "Skipped. I do the hard work around here.",
            ],
            "queue": [
                "Here’s your queue. Try not to cry.",
                "Queue coming up. Brace yourself.",
                "Fine. Here’s the queue. Happy now.",
            ],
            "default": [
                "I heard you. I just chose to ignore you.",
                "Say that again but with better English.",
                "Interesting. Wrong, but interesting.",
            ],

            # 🔥🔥🔥 ROAST MODE 🔥🔥🔥
            "roast": [
                "You really typed that with confidence, huh.",
                "I’d respond, but I don’t speak nonsense fluently.",
                "Your requests are like your WiFi — weak.",
                "Bold of you to assume I care.",
                "I’ve seen potatoes with better decision‑making.",
                "Congrats. That message lowered my IQ.",
                "If bad ideas were a sport, you'd be a champion.",
                "I’d roast you harder, but I don’t want to break you.",
            ],
        }

    def get(self, category: str) -> str:
        # Optional: 10% chance to roast ANY reply
        if random.random() < 0.10:
            return random.choice(self.replies["roast"])

        return random.choice(self.replies.get(category, self.replies["default"]))
