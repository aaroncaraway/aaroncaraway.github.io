---
layout: archive
permalink: /css/
---

## How to add a background image to both the top and the bottom corners

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
