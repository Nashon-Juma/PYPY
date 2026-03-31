# ✅ 1. Sequence Diagram (your main flow)

```mermaid
sequenceDiagram
    participant User
    participant "Portal UI (Inertia + Vue 3 + TS)" as UI
    participant Laravel
    participant DB
    participant Queue
    participant Salesforce

    User->>UI: Compose / autosave / submit
    UI->>Laravel: POST draft or submit
    Laravel->>Laravel: Validate + Policy + EligibilityService
    Laravel->>DB: Save draft/message + transition
    Laravel->>DB: Create outbox event
    Laravel-->>UI: Success response
    Laravel->>Queue: Dispatch notification + sync jobs
    Queue->>Salesforce: Upsert correspondence
    Salesforce-->>Queue: Success / failure
    Queue->>DB: Update sync state
```

---

# ✅ 2. System Architecture (cleaned version)

```mermaid
graph TD

    User --> UI[Portal UI<br/>Inertia + Vue 3 + TypeScript]
    UI --> Laravel[Laravel Application]

    Laravel --> DB[(MySQL)]
    Laravel --> Redis[Redis Cache / Queue]

    Redis --> Workers[Queue Workers / Horizon]

    Laravel --> Storage[BrilliantStorage Adapter]
    Workers --> Storage

    Laravel --> Salesforce[Salesforce Adapter]
    Workers --> Salesforce

    WordPress[WordPress Legacy] --> Jobs[Import + Reconciliation Jobs]
    Jobs --> DB
```

```mermaid
flowchart TB
    subgraph "Core Entities"
        User["User<br/>(uuid, public_key, auth_type: sponsor|staff|admin|child)"]
        Child["Child<br/>(salesforce_contact_id, consent_status, program_status, alumni_date, case_manager_id)"]
        SponsorLink["SponsorLink<br/>(sponsor_user_id, child_id, relationship_type, status, dates)"]
        Thread["CorrespondenceThread<br/>(child_id, sponsor_user_id)"]
        Message["CorrespondenceMessage<br/>(thread_id, sender_id, subject, body, business_status, sync_status, salesforce_id)"]
        Draft["CorrespondenceDraft<br/>(thread_id, sender_id, subject, body, autosave_timestamp)"]
        Attachment["CorrespondenceAttachment<br/>(message_id / draft_id, BrilliantStorage provider)"]
    end

    subgraph "Services"
        Eligibility["CommunicationEligibilityService"]
        Workflow["CorrespondenceWorkflowService"]
    end

    subgraph "Integrations"
        Outbox["IntegrationOutbox<br/>(entity_type, entity_id, event_type, payload, status)"]
        Log["IntegrationLog<br/>(outbox_id, snapshots, retry_count)"]
        Legacy["LegacyMapping"]
    end

    User --> Child
    User --> SponsorLink
    SponsorLink --> Child
    SponsorLink --> Thread
    Thread --> Message
    Thread --> Draft
    Message --> Attachment
    Draft --> Attachment

    Eligibility -.->|"validates"| SponsorLink
    Eligibility -.->|"checks"| Child
    Workflow -.->|"manages"| Draft
    Workflow -.->|"manages"| Message
    Workflow -.->|"records"| WorkflowTransition

    Outbox -.->|"processes"| Queue
    Outbox -.->|"logs"| Log
```
