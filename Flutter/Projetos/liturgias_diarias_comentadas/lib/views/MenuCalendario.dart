import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:liturgias_diarias_comentadas/components/user_tile.dart';
import 'package:liturgias_diarias_comentadas/data/dummy_user.dart';
import 'package:liturgias_diarias_comentadas/models/user.dart';
import 'package:table_calendar/table_calendar.dart';

class Menucalendario extends StatefulWidget {
  const Menucalendario({Key? key}) : super(key: key);

  @override
  State<Menucalendario> createState() => _Menucalendario();
}

DateTime _selectedDay = DateTime.now();

DateFormat formatter = DateFormat('dd/MM/yyyy');
DateFormat formatterNome = DateFormat('MMMM yyyy', 'pt_BR');

// Formatar o DateTime para uma String

class _Menucalendario extends State<Menucalendario> {
  @override
  Widget build(BuildContext context) {
    var theme = Theme.of(context);

    const users = {...dummyUser};


 final List<User> allUsers = users.values.toList();

    // Filtra a lista de usuários com base na data selecionada
    final List<User> filteredUsers = allUsers.where((user) {
     DateTime data =formatter.parse(user.data);
     
      // Comparar apenas a data, ignorando a hora
      return data.year == _selectedDay.year &&
             data.month == _selectedDay.month &&
             data.day == _selectedDay.day;
    }).toList();

    return MaterialApp(
      
      home: Scaffold(
        body: SafeArea(
          child: Expanded(
            child: Column(
              crossAxisAlignment:
                  CrossAxisAlignment
                      .stretch, // Opcional, mas útil para alinhar outros filhos
              children: [
                Expanded(
                  child: Stack(
                    fit:
                        StackFit
                            .expand, // Faz o Stack ocupar todo o espaço do Expanded
                    children: <Widget>[
                      Image.asset(
                        fit: BoxFit.cover,
                        "igreja.jpg",
                       
                      ),
                      Center(
                        // Centraliza o texto (você pode usar outros widgets de posicionamento)
                        child: Text(
                          "Calendário Litúrgico",
                          style: TextStyle(
                            color: Colors.white, // Cor do texto
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),

                TableCalendar(
                  headerVisible: true,
                  headerStyle: HeaderStyle(
                    titleCentered: true,
                    formatButtonVisible: false,
                    titleTextFormatter: (date, locale) {
                      String nomeMes = DateFormat(
                        'MMMM',
                        'pt_BR',
                      ).format(_selectedDay);
                      String ano = DateFormat(
                        'yyyy',
                        'pt_BR',
                      ).format(_selectedDay);

                      String nomeMesCapitalizado =
                          "${nomeMes[0].toUpperCase()}${nomeMes.substring(1)} $ano";
                      return nomeMesCapitalizado;
                    },
                  ),
                  locale: 'pt_BR',
                  calendarFormat: CalendarFormat.twoWeeks,
                  currentDay: _selectedDay,
                  focusedDay: _selectedDay,
                  firstDay: DateTime.utc(2010, 10, 16),
                  lastDay: DateTime.utc(2030, 3, 14),

                  onDaySelected: (selectedDay, focusedDay) {
                    setState(() {
                      _selectedDay = selectedDay;
                      _selectedDay =
                          focusedDay; // update `_selectedDay` here as well
                    });
                  },
                ),
                Expanded(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      Text(
                        "Selected Date",
                        textAlign: TextAlign.center,
                        style: theme.textTheme.titleMedium!.copyWith(
                          color: theme.primaryColor,
                        ),
                      ),
                      const SizedBox(height: 3),

                      /*  Text(
                        DateFormat('dd MMM yyyy').format(_selectedDay),
                        textAlign: TextAlign.center,
                        style: theme.textTheme.titleLarge!.copyWith(
                          color: theme.primaryColor,
                        ),
                      ), */
                    ],
                  ),
                ),
                Expanded(
                  child: ListView.builder(
                    itemCount: filteredUsers.length,
                    itemBuilder: (context, index) {
                      final User user = filteredUsers[index];
                      return UserTile(
                        user,
                      ); // Assuindo que UserTile recebe um objeto User
                    },
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
