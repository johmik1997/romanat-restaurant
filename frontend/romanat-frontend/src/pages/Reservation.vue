<template>
  <div class="max-w-7xl mx-auto p-6">
    <Header
      title="Reservation Management"
      subtitle="Manage all hotel reservations and bookings."
      search-placeholder="Search reservations by guest name, booking ID, or room number..."
      @search="handleSearch"
    />

    <!-- Action Buttons -->
    <div class="flex flex-wrap items-center justify-between gap-4 mb-6">
      <div class="flex flex-1 gap-3 flex-wrap justify-start">
        <ActionButton
          label="Add Reservation"
          icon="add"
          variant="primary"
          @click="openAddModal" 
        />
        <ActionButton
          label="Bulk Check-in"
          icon="login"
          variant="secondary"
          @click="handleBulkCheckIn"
        />
        <ActionButton
          label="Export Reservations"
          icon="download"
          variant="secondary"
          @click="handleExport"
        />
        <ActionButton
          label="Filter Reservations"
          icon="filter_list"
          variant="secondary"
          @click="showFilterDialog = true"
        />
      </div>

      <!-- Date Range Filter -->
      <div class="flex items-center gap-3">
        <div class="flex items-center gap-2">
          <span class="text-sm text-gray-900">From:</span>
          <input
            type="date"
            v-model="dateRange.start"
            @change="handleDateFilter"
            class="px-3 py-2 border text-black border-gray-300 rounded-lg bg-white text-sm focus:ring-2 focus:ring-[#0f766e]/20 focus:border-[#0f766e]"
          />
        </div>
        <div class="flex items-center gap-2">
          <span class="text-sm text-gray-600">To:</span>
          <input
            type="date"
            v-model="dateRange.end"
            @change="handleDateFilter"
            class="px-3 py-2 border text-black border-gray-300 rounded-lg bg-white text-sm focus:ring-2 focus:ring-[#0f766e]/20 focus:border-[#0f766e]"
          />
        </div>
      </div>
    </div>

    <!-- Stats Cards -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <MetricCard label="Total Reservations" :value="reservationStats.total" />
      <MetricCard
        label="Upcoming Check-ins"
        :value="reservationStats.upcoming"
      />
      <MetricCard
        label="Pending Confirmations"
        :value="reservationStats.pending"
      />
      <MetricCard label="Cancelled" :value="reservationStats.cancelled" />
    </section>

    <!-- Reservation Table -->
    <div class="bg-white border border-gray-200 rounded-xl shadow-sm">
      <div class="border-b border-gray-200 px-6">
        <nav class="-mb-px flex space-x-6">
          <button
            v-for="tab in tabs"
            :key="tab.name"
            @click="setActiveTab(tab)"
            :class="tabClasses(tab)"
          >
            {{ tab.name }}
            <span
              v-if="tab.count"
              class="ml-2 bg-gray-200 text-gray-600 text-xs px-2 py-1 rounded-full"
            >
              {{ tab.count }}
            </span>
          </button>
        </nav>
      </div>

      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                <input
                  type="checkbox"
                  v-model="selectAll"
                  @change="toggleSelectAll"
                  class="rounded border-gray-300 text-primary focus:ring-primary"
                />
              </th>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                Booking ID
              </th>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                Guest Name
              </th>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                Check-in / Check-out
              </th>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                Room Type
              </th>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                Guests
              </th>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                Total Amount
              </th>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                Status
              </th>
              <th
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
              >
                Actions
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr
              v-for="reservation in reservations"
              :key="reservation.id"
              class="hover:bg-gray-50 transition-colors duration-150 cursor-pointer"
              @click="goToReservationDetails(reservation.id)"
            >
              <!-- Checkbox -->
              <td class="px-6 py-4 whitespace-nowrap" @click.stop>
                <input
                  type="checkbox"
                  v-model="selectedReservations"
                  :value="reservation.id"
                  class="rounded border-gray-300 text-primary focus:ring-primary"
                />
              </td>

              <!-- Booking ID -->
              <td
                class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
              >
                #{{ reservation.booking_id || reservation.id }}
              </td>

              <!-- Guest Info -->
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                <div class="font-medium">
                  {{
                    reservation.customer.first_name +
                    " " +
                    reservation.customer.last_name
                  }}
                </div>
                <div class="text-gray-500 text-xs">{{ reservation.customer.email }}</div> <!-- Fixed: reservation.customer.email -->
              </td>

              <!-- Dates -->
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                <div class="font-medium">
                  {{ formatDate(reservation.check_in) }}
                </div>
                <div class="text-xs">
                  {{ formatDate(reservation.check_out) }}
                </div>
              </td>

              <!-- Room -->
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                <div class="font-medium">
                  {{ reservation.room.room_type.name }}
                </div>
                <div
                  class="text-xs text-gray-400"
                  v-if="reservation.room.room_number"
                >
                  Room {{ reservation.room.room_number }}
                </div>
                <div class="text-xs text-orange-500" v-else>
                  Room not assigned
                </div>
              </td>

              <!-- Guests -->
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ reservation.number_of_guests }} Guest(s)
              </td>

              <!-- Total -->
              <td
                class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
              >
                ${{ reservation.total_price || "0.00" }}
              </td>

              <!-- Status -->
              <td class="px-6 py-4 whitespace-nowrap text-sm">
                <span
                  :class="statusClasses(reservation.status)"
                  class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
                >
                  {{ formatStatus(reservation.status) }}
                </span>
              </td>

              <!-- Actions -->
              <td
                class="px-6 py-4 whitespace-nowrap text-sm font-medium"
                @click.stop
              >
                <div class="flex items-center justify-end gap-2">
                  <button
                    @click="editReservation(reservation)"
                    class="p-1.5 text-gray-500 rounded hover:bg-gray-100"
                  >
                    <span class="material-symbols-outlined text-green-500 text-xl">edit</span>
                  </button>
                  <button
                    @click="deleteReservation(reservation)"
                    class="p-1.5 text-gray-500 rounded hover:bg-gray-100"
                  >
                    <span class="material-symbols-outlined text-red-500 text-xl">delete</span>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Empty State -->
        <div
          v-if="reservations.length === 0 && !loading"
          class="text-center py-12"
        >
          <span class="material-symbols-outlined text-6xl text-gray-300 mb-4"
            >calendar_month</span
          >
          <h3 class="text-lg font-medium text-gray-900 mb-2">
            No reservations found
          </h3>
          <p class="text-gray-500 mb-4">Try adjusting your search or filters</p>
          <button
            @click="resetFilters"
            class="bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary/90 transition-colors"
          >
            Reset Filters
          </button>
        </div>
      </div>

      <!-- Pagination -->
      <div
        v-if="totalCount > 0"
        class="px-6 py-4 border border-gray-200 rounded-2xl bg-white shadow-sm"
      >
        <div
          class="flex flex-col md:flex-row items-center justify-between gap-4"
        >
          <div class="text-sm text-gray-700">
            Showing
            <span class="font-medium">{{ paginationStart }}</span>
            to
            <span class="font-medium">{{ paginationEnd }}</span>
            of
            <span class="font-medium">{{ totalCount }}</span> reservations
          </div>

          <div class="flex items-center gap-2">
            <button
              @click="previousPage"
              :disabled="currentPage === 1"
              :class="[
                'px-4 py-2 border border-gray-300 rounded-lg font-medium transition-colors',
                currentPage === 1
                  ? 'bg-gray-50 text-gray-400 cursor-not-allowed'
                  : 'bg-white text-gray-700 hover:bg-gray-50 hover:border-gray-400',
              ]"
            >
              Previous
            </button>

            <div class="flex items-center gap-1">
              <button
                v-for="page in visiblePages"
                :key="page"
                @click="goToPage(page)"
                :class="[
                  'w-10 h-10 flex items-center justify-center rounded-lg font-medium transition-colors',
                  currentPage === page
                    ? 'bg-[#0f766e] text-white'
                    : 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50',
                ]"
              >
                {{ page }}
              </button>
              <span v-if="showEllipsis" class="px-2 text-gray-500">...</span>
            </div>

            <button
              @click="nextPage"
              :disabled="currentPage >= totalPages"
              :class="[
                'px-4 py-2 border border-gray-300 rounded-lg font-medium transition-colors',
                currentPage >= totalPages
                  ? 'bg-gray-50 text-gray-400 cursor-not-allowed'
                  : 'bg-white text-gray-700 hover:bg-gray-50 hover:border-gray-400',
              ]"
            >
              Next
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Add/Edit Reservation Modal -->
    <AddEditReservationModal
      :show="showReservationModal"
      :reservation="selectedReservation"
      @close="closeReservationModal"
      @save="handleSaveReservation"
    />

    <!-- Filter Dialog -->
    <div
      v-if="showFilterDialog"
      class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
    >
      <div class="bg-white rounded-lg p-6 w-full max-w-md">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-lg font-semibold text-gray-900">
            Filter Reservations
          </h3>
          <button
            @click="showFilterDialog = false"
            class="text-gray-400 hover:text-gray-600"
          >
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>

        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Status</label
            >
            <select
              v-model="filterCriteria.status"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg"
            >
              <option value="">All Status</option>
              <option value="confirmed">Confirmed</option>
              <option value="checked_in">Checked In</option>
              <option value="checked_out">Checked Out</option>
              <option value="cancelled">Cancelled</option>
              <option value="pending">Pending</option>
            </select>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Date From</label
            >
            <input
              type="date"
              v-model="filterCriteria.dateFrom"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Date To</label
            >
            <input
              type="date"
              v-model="filterCriteria.dateTo"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg"
            />
          </div>
        </div>

        <div class="flex justify-end gap-3 mt-6">
          <button
            @click="resetFilter"
            class="px-4 py-2 text-gray-700 border border-gray-300 rounded-lg hover:bg-gray-50"
          >
            Reset
          </button>
          <button
            @click="applyFilter"
            class="px-4 py-2 bg-primary text-white rounded-lg hover:bg-primary/90"
          >
            Apply Filters
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "../components/staffs/Headers.vue";
import MetricCard from "../components/staffs/MetricCard.vue";
import ActionButton from "../components/staffs/ActionButton.vue";
import AddEditReservationModal from "../components/modal/AddEditReservationModal.vue"; // Renamed import
import {
  createReservation,
  getReservations,
  updateReservationStatus,
  updateReservation,  // Added this
  deleteReservation   // Added this
} from "../api/auth/reservation";

export default {
  name: "Reservations",
  components: {
    Header,
    MetricCard,
    ActionButton,
    AddEditReservationModal, // Changed component registration
  },
  data() {
    return {
      showReservationModal: false, // Changed from showAddModal
      showFilterDialog: false,
      loading: false,
      activeTab: "all",
      selectAll: false,
      currentPage: 1,
      itemsPerPage: 10,
      totalCount: 0,
      selectedReservations: [],
      searchQuery: "",
      dateRange: {
        start: "",
        end: "",
      },
      filterCriteria: {
        status: "",
        dateFrom: "",
        dateTo: "",
      },
      tabs: [
        { name: "All", key: "all", count: 0 },
        { name: "Confirmed", key: "confirmed", count: 0 },
        { name: "Checked-in", key: "checked_in", count: 0 },
        { name: "Checked-out", key: "checked_out", count: 0 },
        { name: "Cancelled", key: "cancelled", count: 0 },
      ],
      reservationStats: {
        total: 0,
        upcoming: 0,
        pending: 0,
        cancelled: 0,
      },
      reservations: [],
      selectedReservation: null, // Added for edit mode
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.totalCount / this.itemsPerPage);
    },
    paginationStart() {
      return this.totalCount === 0
        ? 0
        : (this.currentPage - 1) * this.itemsPerPage + 1;
    },
    paginationEnd() {
      return Math.min(this.currentPage * this.itemsPerPage, this.totalCount);
    },
    visiblePages() {
      const pages = [];
      const maxVisible = 5;
      let start = Math.max(1, this.currentPage - Math.floor(maxVisible / 2));
      let end = Math.min(this.totalPages, start + maxVisible - 1);

      if (end - start + 1 < maxVisible) {
        start = Math.max(1, end - maxVisible + 1);
      }

      for (let i = start; i <= end; i++) {
        pages.push(i);
      }
      return pages;
    },
    showEllipsis() {
      return (
        this.totalPages > this.visiblePages.length &&
        this.visiblePages[this.visiblePages.length - 1] < this.totalPages
      );
    },
  },
  async mounted() {
    await this.loadReservations();
  },
  methods: {
    async loadReservations() {
      this.loading = true;
      try {
        // Build query params for API
        const params = {
          page: this.currentPage,
          page_size: this.itemsPerPage,
          ordering: '-created_at' // Added default ordering
        };

        // Add search query
        if (this.searchQuery.trim()) {
          params.search = this.searchQuery.trim();
        }

        // Add status filter from active tab
        if (this.activeTab !== "all") {
          params.status = this.activeTab;
        }

        // Add date range filters - Use correct parameter names for your backend
        if (this.dateRange.start) {
          params.check_in__gte = this.dateRange.start; // Changed from check_in_from
        }
        if (this.dateRange.end) {
          params.check_in__lte = this.dateRange.end; // Changed from check_in_to
        }

        // Add additional filter criteria
        if (this.filterCriteria.status) {
          params.status = this.filterCriteria.status;
        }
        if (this.filterCriteria.dateFrom) {
          params.check_in__gte = this.filterCriteria.dateFrom; // Changed from check_in_from
        }
        if (this.filterCriteria.dateTo) {
          params.check_in__lte = this.filterCriteria.dateTo; // Changed from check_in_to
        }

        console.log('Loading reservations with params:', params); // Debug log

        // Call API with params
        const response = await getReservations(params);

        console.log('API Response:', response); // Debug log

        // Handle your specific backend response format:
        // { count: 11, page: 1, number_of_pages: 2, result: [...] }
        if (response && response.result !== undefined) {
          this.reservations = response.result || [];
          this.totalCount = response.count || 0;
        } else if (response && Array.isArray(response.results)) {
          // Django REST Framework pagination format
          this.reservations = response.results;
          this.totalCount = response.count || 0;
        } else if (Array.isArray(response)) {
          // Simple array response
          this.reservations = response;
          this.totalCount = response.length;
        } else {
          console.warn("Unexpected API response format:", response);
          this.reservations = [];
          this.totalCount = 0;
        }

        this.updateStats();
      } catch (error) {
        console.error("Error loading reservations:", error);
        this.reservations = [];
        this.totalCount = 0;
        
        // Only use sample data for debugging in development
        if (process.env.NODE_ENV === "development") {
          console.log("Using sample data for development");
          this.reservations = this.getSampleReservations();
          this.totalCount = this.reservations.length;
          this.updateStats();
        }
      } finally {
        this.loading = false;
      }
    },

    updateStats() {
      // Calculate stats from current page results
      const stats = {
        total: this.totalCount,
        upcoming: this.reservations.filter((r) => r.status === "confirmed").length,
        pending: this.reservations.filter((r) => r.status === "pending").length,
        cancelled: this.reservations.filter((r) => r.status === "cancelled").length,
      };

      this.reservationStats = stats;

      // Update tab counts based on current page results
      this.tabs = this.tabs.map((tab) => ({
        ...tab,
        count:
          tab.key === "all"
            ? this.totalCount
            : this.reservations.filter((r) => r.status === tab.key).length,
      }));
    },

    getSampleReservations() {
      return [
        {
          id: 1,
          booking_id: "RES001",
          customer: { 
            id: 1,
            first_name: "John", 
            last_name: "Smith",
            email: "john.smith@email.com" 
          },
          check_in: "2024-01-15",
          check_out: "2024-01-18",
          room: {
            room_type: { name: "Deluxe King" },
            room_number: "301",
          },
          number_of_guests: 2,
          total_price: "450.00",
          status: "confirmed",
        },
        {
          id: 2,
          booking_id: "RES002",
          customer: { 
            id: 2,
            first_name: "Sarah", 
            last_name: "Johnson",
            email: "sarah.j@email.com" 
          },
          check_in: "2024-01-20",
          check_out: "2024-01-22",
          room: {
            room_type: { name: "Standard Queen" },
            room_number: null,
          },
          number_of_guests: 1,
          total_price: "300.00",
          status: "pending",
        },
      ];
    },

    handleSearch(query) {
      this.searchQuery = query;
      this.currentPage = 1;
      this.loadReservations();
    },

    // Add button handler
    openAddModal() {
      this.selectedReservation = null;
      this.showReservationModal = true;
    },

    editReservation(reservation) {
      console.log("Edit reservation:", reservation);
      this.selectedReservation = reservation;
      this.showReservationModal = true;
    },

    // Delete button handler
    async deleteReservation(reservation) {
      if (confirm(`Are you sure you want to delete reservation #${reservation.booking_id || reservation.id}? This action cannot be undone.`)) {
        try {
          await deleteReservation(reservation.id);
          await this.loadReservations();
          alert("Reservation deleted successfully!");
        } catch (error) {
          console.error("Error deleting reservation:", error);
          alert("Failed to delete reservation. Please try again.");
        }
      }
    },

    // Close modal handler
    closeReservationModal() {
      this.showReservationModal = false;
      this.selectedReservation = null;
    },

    // Save/Update reservation handler
    async handleSaveReservation(reservationData) {
      try {
        if (reservationData.id) {
          // Update existing reservation
          await updateReservation(reservationData.id, reservationData);
          alert("Reservation updated successfully!");
        } else {
          // Create new reservation
          await createReservation(reservationData);
          alert("Reservation created successfully!");
        }

        // Reload reservations
        await this.loadReservations();
        this.closeReservationModal();
      } catch (error) {
        console.error("Error saving reservation:", error);
        alert(`Failed to ${reservationData.id ? "update" : "create"} reservation. Please try again.`);
      }
    },

    // Keep this for backward compatibility
    async handleAddReservation(newReservation) {
      await this.handleSaveReservation(newReservation);
    },

    async handleBulkCheckIn() {
      if (!this.selectedReservations.length) {
        alert("Please select reservations to check in.");
        return;
      }

      try {
        for (const id of this.selectedReservations) {
          await updateReservationStatus(id, "checked_in");
        }

        await this.loadReservations();
        const count = this.selectedReservations.length; // Store count before clearing
        this.selectedReservations = [];
        alert(`${count} reservations checked in successfully!`);
      } catch (err) {
        console.error("Bulk check-in failed:", err);
        alert("Failed to check in reservations. Please try again.");
      }
    },

    handleExport() {
      const dataToExport = this.reservations;

      if (!dataToExport.length) {
        alert("No reservations to export.");
        return;
      }

      // Convert to CSV
      const headers = [
        "Reservation ID",
        "Guest Name",
        "Status",
        "Check-In",
        "Check-Out",
        "Total Price",
      ];
      const rows = dataToExport.map((r) => [
        `#${r.booking_id || r.id}`,
        `${r.customer.first_name} ${r.customer.last_name}`,
        this.formatStatus(r.status),
        r.check_in,
        r.check_out,
        `$${r.total_price}`,
      ]);

      const csvContent = [headers, ...rows].map((e) => e.join(",")).join("\n");

      // Create downloadable file
      const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.setAttribute(
        "download",
        `reservations_${new Date().toISOString().split("T")[0]}.csv`
      );
      link.click();
    },

    handleFilter() {
      this.showFilterDialog = true;
    },

    applyFilter() {
      this.currentPage = 1;
      this.activeTab = this.filterCriteria.status || "all";
      this.loadReservations();
      this.showFilterDialog = false;
    },

    resetFilter() {
      this.filterCriteria = {
        status: "",
        dateFrom: "",
        dateTo: "",
      };
      this.dateRange = {
        start: "",
        end: "",
      };
      this.activeTab = "all";
      this.searchQuery = "";
      this.currentPage = 1;
      this.loadReservations();
      this.showFilterDialog = false;
    },

    handleDateFilter() {
      if (this.dateRange.start && this.dateRange.end) {
        this.currentPage = 1;
        this.loadReservations();
      }
    },

    setActiveTab(tab) {
      this.activeTab = tab.key;
      this.currentPage = 1;
      this.loadReservations();
    },

    tabClasses(tab) {
      return [
        "whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm flex items-center transition-colors duration-200",
        this.activeTab === tab.key
          ? "border-primary text-primary"
          : "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300",
      ];
    },

    statusClasses(status) {
      const statusMap = {
        confirmed: "bg-blue-100 text-blue-800",
        checked_in: "bg-green-100 text-green-800",
        checked_out: "bg-gray-100 text-gray-800",
        cancelled: "bg-red-100 text-red-800",
        pending: "bg-yellow-100 text-yellow-800",
      };

      return statusMap[status] || "bg-gray-100 text-gray-800";
    },

    formatStatus(status) {
      const statusMap = {
        confirmed: "Confirmed",
        checked_in: "Checked In",
        checked_out: "Checked Out",
        cancelled: "Cancelled",
        pending: "Pending",
      };
      return statusMap[status] || status;
    },

    toggleSelectAll() {
      if (this.selectAll) {
        this.selectedReservations = this.reservations.map((r) => r.id);
      } else {
        this.selectedReservations = [];
      }
    },

    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
        this.loadReservations();
      }
    },

    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
        this.loadReservations();
      }
    },

    goToPage(page) {
      if (page !== this.currentPage) {
        this.currentPage = page;
        this.loadReservations();
      }
    },

    goToReservationDetails(id) {
      this.$router.push(`/staff/reservation/${id}`);
    },

    formatDate(dateString) {
      if (!dateString) return "N/A";
      const date = new Date(dateString);
      return date.toLocaleDateString("en-US", {
        month: "short",
        day: "numeric",
        year: "numeric",
      });
    },

    resetFilters() {
      this.resetFilter();
    },
  },
  watch: {
    selectedReservations(newVal) {
      this.selectAll =
        newVal.length === this.reservations.length &&
        this.reservations.length > 0;
    },
  },
};
</script>