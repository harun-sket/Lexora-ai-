import './style.css'

document.querySelector('#app').innerHTML = `
  <header class="navbar">
    <div class="logo">LEXORA</div>

    <nav>
      <a href="#platform">Platform</a>
      <a href="#api">API</a>
      <a href="#docs">Docs</a>
      <a href="#pricing">Pricing</a>
    </nav>

    <div class="nav-actions">
      <button class="btn btn-ghost">Sign in</button>
      <button class="btn btn-primary">Get started</button>
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="badge">LANGUAGE INTELLIGENCE INFRASTRUCTURE</div>

      <h1>
        Turn messy raw data
        <span>into AI-ready intelligence.</span>
      </h1>

      <p class="hero-text">
        Lexora is building India's language intelligence layer
        for the future of AI.
      </p>

      <div class="hero-actions">
        <button class="btn btn-primary btn-large">
          Start building
        </button>

        <button class="btn btn-outline btn-large">
          Explore API
        </button>
      </div>

      <div class="status">
        <span class="status-dot"></span>
        Lexora Engine V1.0 operational
      </div>
    </section>

    <section class="stats" id="platform">
      <div class="stat">
        <strong>1M+</strong>
        <span>words stress tested</span>
      </div>

      <div class="stat">
        <strong>4M</strong>
        <span>tokens tested</span>
      </div>

      <div class="stat">
        <strong>20×</strong>
        <span>concurrent requests tested</span>
      </div>

      <div class="stat">
        <strong>V1.0</strong>
        <span>engine</span>
      </div>
    </section>

    <section class="features" id="api">
      <div class="section-heading">
        <div class="badge">THE PLATFORM</div>

        <h2>Language intelligence, built for machines.</h2>

        <p>
          Process raw language and transform it into
          structured, AI-ready information.
        </p>
      </div>

      <div class="feature-grid">
        <article class="feature-card">
          <div class="feature-number">01</div>
          <h3>Language Processing</h3>
          <p>
            Tokenization and linguistic analysis through
            the Lexora engine.
          </p>
        </article>

        <article class="feature-card">
          <div class="feature-number">02</div>
          <h3>AI-Ready Data</h3>
          <p>
            Transform messy language data into predictable,
            machine-readable output.
          </p>
        </article>

        <article class="feature-card">
          <div class="feature-number">03</div>
          <h3>Developer API</h3>
          <p>
            Integrate Lexora intelligence into applications
            through a simple API.
          </p>
        </article>
      </div>
    </section>

    <section class="api-preview" id="docs">
      <div>
        <div class="badge">LEXORA API</div>

        <h2>One engine. One API.</h2>

        <p>
          Send language data. Receive structured intelligence.
        </p>
      </div>

      <pre><code>POST /v1/analyze

{
  "text": "உங்கள் உரை இங்கே"
}</code></pre>
    </section>

    <section class="cta" id="pricing">
      <div class="badge">BUILD WITH LEXORA</div>

      <h2>Ready to build the language layer?</h2>

      <button class="btn btn-primary btn-large">
        Get started
      </button>
    </section>
  </main>

  <footer>
    <div>© 2026 Lexora</div>
    <div>Language intelligence infrastructure.</div>
  </footer>
`
