import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:teste/provider/users.dart';
import 'package:teste/views/user_list.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {

    return ChangeNotifierProvider(
      create: (ctx)=>UsersProvider(),
      child: MaterialApp(
        title: "Flutter Demo",
        color: Colors.blue,
        theme: ThemeData(
          primaryColor: Colors.blue,
          visualDensity: VisualDensity.adaptivePlatformDensity),
          home: UserList(),
          debugShowCheckedModeBanner: false,      
      ),
    );
  }
}
