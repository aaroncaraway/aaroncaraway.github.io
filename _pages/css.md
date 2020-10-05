---
layout: archive
permalink: /css/
---

## How to add a background image to both the top and the bottom corners

### BEST ATTEMPT

[SEE MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/background-position)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <style>
      body {
        background-image: url("images/bg-pattern-top-mobile.svg"),
          url("images/bg-pattern-bottom-mobile.svg");
        background-position: 0px 0px, right 0em bottom 0em;
        background-repeat: no-repeat, no-repeat;
        min-height: 100vh;
      }

      @media (min-width: 992px) {
        body {
          background-image: url("images/bg-pattern-top-desktop.svg"),
            url("images/bg-pattern-bottom-desktop.svg");
        }
      }
    </style>
    <h1>hello there!</h1>
  </body>
</html>
```

### FIRST ATTEMPT

```css
body {
  color: hsl(300, 43%, 22%);
  font-family: "Spartan", sans-serif;
  font-size: 15px;
  line-height: 1.25rem;
  height: 100%;
  background-color: #fff;
  background-image: url("images/bg-pattern-bottom-mobile.svg");
  background-position: right bottom;
  background-repeat: no-repeat;
}
.inner-container {
  background-image: url("images/bg-pattern-top-mobile.svg");
  background-repeat: no-repeat;
  height: 50vh;
}
@media (min-width: 992px) {
  body {
    background-image: url("images/bg-pattern-bottom-desktop.svg");
  }
  .inner-container {
    background-image: url("images/bg-pattern-top-desktop.svg");
  }
}
```
