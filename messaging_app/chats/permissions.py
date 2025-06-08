from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to allow only participants of the conversation
    to access and modify messages.
    """

    def has_permission(self, request, view):
        # Allow only authenticated users to access the API
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        # Assuming obj is a Message or Conversation instance and has a conversation attribute

        conversation = getattr(obj, 'conversation', None)
        if conversation is None:
            # If obj is a Conversation instance itself
            conversation = obj

        # Check if the requesting user is a participant of the conversation
        return request.user in conversation.participants.all()
