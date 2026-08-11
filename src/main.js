import './style.css'

document.querySelector('#app').innerHTML = `
  <header class="navbar">

    <a class="logo" href="/">LEXORA</a>

    <nav>
      <a href="/platform.html">Platform</a>
      <a href="/api.html">API</a>
      <a href="/docs.html">Docs</a>
      <a href="/pricing.html">Pricing</a>
    </nav>

    <div class="nav-actions">
      <a class="btn btn-ghost" href="/auth.html">
        Sign in
      </a>

      <a class="btn btn-primary" href="/auth.html">
        Get started
      </a>
    </div>

  </header>

  <main>

    <section class="hero">

      <div class="badge">
        LANGUAGE INTELLIGENCE INFRASTRUCTURE
      </div>

      <h1>
        Turn messy raw
        <span>data into AI-ready intelligence.</span>
      </h1>

      <p class="hero-text">
        Lexora is building India's language intelligence layer
        for the future of AI.
      </p>

      <div class="hero-actions">

        <a
          class="btn btn-primary btn-large"
          href="/auth.html"
        >
          Start building
        </a>

        <a
          class="btn btn-outline btn-large"
          href="/api.html"
        >
          Explore API
        </a>

      </div>

      <div class="status">
        <span class="status-dot"></span>
        Lexora Engine V1.0 operational
      </div>

    </section>

  </main>

  <footer>
    <div>© 2026 Lexora</div>
    <div>Language intelligence infrastructure.</div>
  </footer>
`
