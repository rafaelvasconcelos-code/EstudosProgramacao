import 'package:flutter/material.dart';
import 'package:teste/components/user_tile.dart';
import 'package:teste/data/dummy_user.dart';

class UserList extends StatelessWidget {
  const UserList({super.key});

  @override
  Widget build(BuildContext context) {
    const users = {...dummyUser};

    return Scaffold(
      appBar: AppBar(
        title: Center(child: Text("Lista de Usuarios")),
        actions: [IconButton(onPressed: () {}, icon: Icon(Icons.add))],
      ),
      body: ListView.builder(
        itemCount: users.length,
        itemBuilder: (ctx, i) => UserTile(users.values.elementAt(i)),
      ),
    );
  }
}
