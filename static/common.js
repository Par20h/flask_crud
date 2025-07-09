$(function () {
  $(".container").on("click", ".updatebtn", function (e) {
    e.preventDefault();
    if ($("#myForm").valid()) {
      const studentData = {
        id: $(this).attr("id"),
        first_name: $("#first_name").val().trim(),
        last_name: $("#last_name").val().trim(),
        dob: $("#dob").val(),
        email: $("#email").val().trim(),
      };
      console.log(studentData);
      $.ajax({
        url: `/update_api/${studentData.id}`,
        method: "PUT",
        contentType: "application/json",
        data: JSON.stringify(studentData),
        success: function (response) {
          console.log("User data updated successfully:", response);
          window.location.href = "/";
        },
        error: function (xhr, status, error) {
          console.error("Error updating user data:", error);
        },
      });
    }
  });

  const table = $("#datatable").DataTable({
    ajax: {
      url: "/list_students_api",
      dataSrc: "",
    },
    pageLength: 10,

    columns: [
      {
        order: "asc",
        data: null,
        render: (data, type, row, meta) => meta.row + 1,
        className: "text-right",
      },
      {
        data: null,
        render: (row) => `${row.first_name} ${row.last_name}`,
      },
      {
        data: "dob",
      },
      {
        data: "email",
      },
      {
        data: null,
        orderable: false,
        searchable: false,
        render: (row) => ` 
        <a href='/update/${row.id}'><button type="button" class="btn btn-outline-dark btn-sm">Update</button></a>
        <button class="btn btn-outline-dark btn-sm dltbtn" data-id="${row.id}">Delete</button> `,
      },
    ],
  });

  $("#datatable tbody").on("click", ".dltbtn", function (e) {
    e.preventDefault();
    const btn = $(this);
    const stuid = btn.data("id");
    console.log(stuid);
    if (confirm("Are You Sure You Want To Delete This Student Data...!!!")) {
      $.ajax({
        url: `/delete_api/${stuid}`,
        type: "DELETE",
        success: function (response) {
          console.log(`Student Data deleted`);
          table.row(btn.parents("tr")).remove().draw(false);
        },
        error: function (xhr, status, error) {
          console.log(`Student Data Not deleted - ${stuid}`);
          alert("Error deleting item: " + xhr.responseJSON.message);
        },
      });
    }
  });

  $(".container").on("click", "#regbtn", function (e) {
    e.preventDefault();
    if ($("#myForm").valid()) 
    {
      const studentData = 
      {
      first_name: $("#first_name").val().trim(),
      last_name: $("#last_name").val().trim(),
      dob: $("#dob").val(),
      email: $("#email").val().trim(),
      };

    console.log(studentData);
    $.ajax({
      url: "/register_api",
      method: "POST",
      contentType: "application/json",
      data: JSON.stringify(studentData),
      success: function (response) {
        console.log("User Created successfully:", response);
        window.location.href = "/";
      },
      error: function (xhr, status, error) 
      {
        console.error("Error Creating user data:", error);
      },
    });
    }
    
  }); 
});
