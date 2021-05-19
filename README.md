## Endpoints

- List & Create All Chats                       /api/chat/ [GET,POST]
- Chat Detail                                   /api/chat/<chat_id> [GET]
- List All Messages                             /api/chat/messages/ [GET]
- Post Message to a ChatRoom                    /api/chat/messages/?chat_id=<room_chat_id> [POST]
- Add or remove user friends                    /api/users/<friend_username>/toggle/ [GET]
- User details                                  /api/users/<username>/ [GET]
- Get Token/Login                               /api/auth/jwt/ [POST]
- Register                                      /api/auth/jwt/register [POST]
- Refresh Token                                 /api/auth/jwt/refresh [POST]    
