---
layout: page
title: Kalender
---

{% assign events = site.data.calender | sort: "date" %}

<table>
  <thead>
    <tr>
      <th>Datum</th>
      <th>Zeit</th>
      <th>Termin</th>
      <th>Ort</th>
    </tr>
  </thead>
  <tbody>
    {% for e in events %}
    <tr>
      <td>{{ e.date | date: "%d.%m.%Y" }}</td>
      <td>{{ e.time }}</td>
      <td>
        {{ e.title }}
        {% if e.type == "deadline" %}
          <strong>(Deadline)</strong>
        {% endif %}
      </td>
      <td>{{ e.location }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

