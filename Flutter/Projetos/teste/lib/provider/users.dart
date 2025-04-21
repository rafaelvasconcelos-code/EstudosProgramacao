import 'package:flutter/material.dart';
import 'package:teste/data/dummy_user.dart';
import 'package:teste/models/user.dart';

class UsersProvider with ChangeNotifier {
  final Map<String, User> _items = {...dummyUser};

  List<User> get all {
    return [..._items.values];
  }

  int get count {
    return _items.length;
  }
}