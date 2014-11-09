from .notification import NotificationProtocolEntity
from Yowsup.structs import ProtocolTreeNode
from Yowsup.structs.protocolentity import ProtocolEntityTest

class NotificationProtocolEntityTest(ProtocolEntityTest):
    def setUp(self):
        self.ProtocolEntity = NotificationProtocolEntity
        attribs = {
            "t": "12345",
            "from": "from_jid",
            "offline": "0",
            "type": "notif_type",
            "id": "message-id",
            "notify": "notify_name"
        }
        self.node = ProtocolTreeNode("notification", attribs)