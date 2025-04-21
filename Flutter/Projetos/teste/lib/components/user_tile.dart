import 'package:flutter/material.dart';
import 'package:teste/models/user.dart';

class UserTile extends StatelessWidget {
  final User user;

  const UserTile(this.user, {super.key});

  @override
  Widget build(BuildContext context) {
    final avatar =
        user.avatarURL.isEmpty || user.avatarURL == ""
            ? CircleAvatar(child: Icon(Icons.person))
            : CircleAvatar(backgroundImage: NetworkImage(user.avatarURL));

    return ListTile(
      leading: avatar,
      title: Text(user.name),
      subtitle: Text(user.email),
     trailing: SizedBox(
      width: 100,
       child: Row(
          children: [
            IconButton(onPressed: () {}, icon: Icon(Icons.edit,color: Colors.orange,)),
            IconButton(onPressed: () {}, icon: Icon(Icons.delete,color: Colors.red,)),
          ],
        ),
     ),
    );
  }
}
