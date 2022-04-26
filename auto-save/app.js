const app = Vue.createApp({
  data() {
    return {
      message: "Auto-Saving",
      showMsg: false,
      timer: null,
    };
  },
  methods: {
    isNumber(evt) {
      evt = evt ? evt : window.event;
      const charCode = evt.which ? evt.which : evt.keyCode;
      if (
        charCode > 31 &&
        (charCode < 48 || charCode > 57) &&
        charCode !== 46
      ) {
        evt.preventDefault();
      } else {
        return true;
      }
    },
    autoSave(evt) {
      if (this.isNumber(evt)) {
        clearTimeout(this.timer);

        this.timer = setTimeout(() => {
          this.showMsg = true;
          this.save();
        }, 2000);
      }
    },
    save() {
      console.log("Calling Backend...");
      clearTimeout(this.timer);

      this.timer = setTimeout(() => {
        this.message = "Saved!";
        this.hideMsg();
      }, 1000);
    },
    hideMsg() {
      clearTimeout(this.timer);

      this.timer = setTimeout(() => {
        this.showMsg = false;
        this.message = "Auto-Saving";
      }, 1000);
    },
  },
});

app.mount("#app");
