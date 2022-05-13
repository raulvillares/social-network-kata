from mamba import description, context, it
from expects import expect, equal

from social_network import SocialNetwork
from user import User

with description("Timeline acceptance tests"):
    with context("given user Bob and user Alice"):
        with it("should allow Bob to read Alice's posts"):
            alice = User("Alice")
            bob = User("Bob ")
            socialNetwork = SocialNetwork()
            socialNetwork.add_user(alice)
            socialNetwork.add_user(bob)
            socialNetwork.post(alice, "First post")
            socialNetwork.post(alice, "Second post")

            result = socialNetwork.getPosts(bob, alice)

            expect(result).to(equal(["First post", "Second post"]))

    with context("given user Charlie follows user Alice and user Bob"):
        with it("should show and aggregate timeline"):
            charlie = User("Charlie")
            alice = User("Alice")
            bob = User("Bob ")
            socialNetwork = SocialNetwork()
            socialNetwork.add_user(alice)
            socialNetwork.add_user(bob)
            socialNetwork.add_user(charlie)
            socialNetwork.follow(charlie, alice)
            socialNetwork.follow(charlie, bob)
            socialNetwork.post(alice, "First post")
            socialNetwork.post(alice, "Second post")
            socialNetwork.post(bob, "Third post")

            result = socialNetwork.timeline(charlie)

            expect(result).to(equal(["First post", "Second post", "Third post"]))