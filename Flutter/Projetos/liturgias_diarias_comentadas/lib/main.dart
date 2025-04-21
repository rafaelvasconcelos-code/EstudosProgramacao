import 'package:flutter/material.dart';
import 'package:liturgias_diarias_comentadas/views/MenuCalendario.dart';
import 'package:intl/date_symbol_data_local.dart';

void main() {

  initializeDateFormatting().then((_) => runApp(MainApp()));
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(
        body: Center(
          child: Menucalendario(),
        ),
      ),
    );
  }
}
